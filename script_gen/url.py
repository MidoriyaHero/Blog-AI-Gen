from django.urls import path
from . import views
urlpatterns =[
    path('',views.index, name = 'index'),
    path('login',views.userlogin, name = 'login'),
    path('signup',views.usersignup, name = 'signup'),
    path('logout',views.userlogout, name = 'logout'),
    path('gen_script', views.gen_script, name = 'gen_script'),
    path('all_blogs', views.all_blogs, name = 'all_blogs'),
    path('detail-blog/<int:pk>', views.blog_detail, name = 'detail-blog')
]