from optparse import AmbiguousOptionError
from django.urls import path 
from .  import views 
from .views import Articledetailview,Createblog,Homeview

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('signin',views.Signin,name="Signin"),
    path('signup',views.Signup,name="signup"),
    path('Contactus',views.Contactus,name="ContactUs"),
    path('Home',Homeview.as_view(),name="Homeview"),
    path('Createblog',Createblog.as_view(),name="Createblog"),
    path('Article/<str:char>',Articledetailview.as_view(),name="Articledetailview"),
    path('politics',views.politics,name="politics"),
    path('business',views.business,name='business'),
    path('entertainment',views.Entertainment,name='entertainment'),
    path('fashion',views.fashion,name='fashion'),
    path('music',views.music,name='music'),
    path('sports',views.sports,name='sports'),
    path('Logout',views.logout,name='Logout'),
]


