from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.Post

admin.site.register(models.Post)
