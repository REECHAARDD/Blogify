from optparse import AmbiguousOptionError
from django.urls import path 
from .  import views 
from .views import Articledetailview, Blog,Createblog

urlpatterns = [
    path('',views.index,name="index"),
    path('signin',views.Signin,name="Signin"),
    path('signup',views.Signup,name="signup"),


   
    path('Home',views.Blog,name="Home"),
    path('Createblog',Createblog.as_view(),name="Createblog"),
    path('Article/<str:char>',Articledetailview.as_view(),name="Articledetailview"),


    path('politics',views.politics,name="politics"),
    path('business',views.business,name='business'),
    path('entertainment',views.Entertainment,name='entertainment'),
    path('fashion',views.fashion,name='fashion'),
    path('music',views.music,name='music'),
    path('sports',views.sports,name='sports'),
    path('Logout',views.logout,name='Logout'),

    path('about',views.about,name="about"),
    path('Contactus',views.Contactus,name="ContactUs"),
]
