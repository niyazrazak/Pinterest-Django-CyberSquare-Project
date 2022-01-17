from django.urls import path
from .import views

urlpatterns = [
    path('', views.fnIndex, name="index"),
    path('head/', views.fnHead, name="head"),
    path('signup/', views.fnSignUp, name="signup"),
    path('signin/', views.fnSignIn, name="signin"),
    path('main/', views.fnMain, name="main"),
    path('userhome/', views.fnHome, name="userhome"),
    path('mypost/', views.fnMypost, name="mypost"),
    path('addpost/', views.fnAddpost, name="addpost"),
    path('addpin/', views.fnAddPin, name="addpin"),
    path('editpin/<pid>', views.fnEditPin, name="editpin"),
    path('deletepin/<pid>', views.fnDeletePin, name="deletepin"),
    path('editpost/<pid>', views.fnEditPost, name="editpost"),
    path('readpin/<pid>', views.fnReadPost, name="readpin"),
    path('readonly/<pid>', views.fnReadOnly, name="readonly"),
    path('readpinlike/<int:pk>', views.BlogPostLike, name="readpinlike"),
    path('postcomment/<int:pk>', views.fnComments, name="postcomment"),
    path('myprofile/', views.fnProfile, name="myprofile"),
    path('logout/', views.fnLogout, name="logout"),
]
