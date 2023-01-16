from django.contrib import admin
from .models import Post, Comments, Message


admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Message)
