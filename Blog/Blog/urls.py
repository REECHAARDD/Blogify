from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import Settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blogify.urls')),
    path('accounts/',include('allauth.urls'))
]# ]+ static(Settings.MEDIA_URL,document_root=Settings.MEDIA_ROOT)
