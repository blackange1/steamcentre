from django.contrib import admin

from .models import Profile, Comment, SubComment

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(SubComment)
