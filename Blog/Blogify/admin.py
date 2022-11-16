from django.contrib import admin
from Blogify.models import post,Preview,SignUp,signin




class form_admin(admin.ModelAdmin):
    admin.site.register(SignUp)


class form_admin(admin.ModelAdmin):
    admin.site.register(signin)

class post(admin.ModelAdmin):
    admin.site.register(post)


class Preview(admin.ModelAdmin):
    admin.site.register(Preview)

