from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('signin', views.signin, name='signin'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),

    
]