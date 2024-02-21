from django.contrib import admin
from .models import User, Profile, Project, Task, Document, Comment
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Document)
admin.site.register(Comment)
