from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Create your views here.
load_dotenv()

@login_required
def index(request):
    return render(request, 'index.html')

def userlogin(request):
    if request.method == 'POST':
        Username = request.POST.get('UserName')
        Password = request.POST.get('Pass')
        user = authenticate(username = Username,password = Password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            Errormessage = 'Invalid username or password!'
            return render(request, 'login.html',{'Errormessage':Errormessage})
    return render(request, 'login.html')

def usersignup(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Username = request.POST.get('Username')
        Passw = request.POST.get('Pass')
        repass = request.POST.get('rePass')
        if Passw == repass:
            try:
                user = User.objects.create_user(email=Email, username=Username, password = Passw)
                user.save()
                login(request, user)
                return  redirect('/')
            except: 
                Errormessage = 'Something went wrong! Please try again!'
                return  render(request,'signup.html', {'Errormessage': Errormessage})
        else:
            Errormessage = 'Passwords do not match! Please check your password and try again!'
            return  render(request,'signup.html', {'Errormessage': Errormessage})
        

    return render(request, 'signup.html')

def userlogout(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def gen_script(request):
    if request.method == 'POST':
        try: 
            data = json.load(request.body)
            link = data['link']
        except (KeyError, json.JSONDecodeError): 
            return JsonResponse({'Error': 'Invalid data link'}, status = 400)
        
        #Get ytb title
        title = yt_title(link)
        #Get script
        transcript = get_transcript(extract_youtube_id(link))
        if not transcript:
            return JsonResponse({'Error': 'Fail to get transcript'}, status =500)
        #Use gemini to generate transcript
        content, _, _ = get_ai_extract(transcript)
        if not content:
            return JsonResponse({'Error': 'Fail to get transcript'}, status =500)
        #save blog 

        #return blog
        return JsonResponse({'Content': content})
    else:
        return JsonResponse({'Error': 'Invalid request method'}, status = 405)
    
def yt_title(link):
    yt = YouTube(link)
    title = yt.title
    return title

def get_transcript(video_id, languages=['en','en-US','en-GB']):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    transcript = TextFormatter().format_transcript(transcript)
    return transcript

# Extract information from text based on prompt instructions
def get_ai_extract(text):
    GEMINI_API = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API)
    genai_model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f'You are the expert in writing blog posts. Here is a transcription of youtube video \n\n {text}\n\n. Your task is to write a comprehensive blog article base on the given transcript and do not make it look like a youtube video, make it look like a proper blog article.'
    response = genai_model.generate_content(prompt, stream=False)
    return response.text, response.prompt_feedback, response.candidates

def extract_youtube_id(url):
    # Split the URL at "watch?v=" and return the part after it
    return url.split("watch?v=")[-1]

