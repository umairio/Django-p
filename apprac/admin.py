from django.contrib import admin
from .models import User, Profile, Project, Task, Document
from django.http import HttpResponseRedirect
from django.core import management
from django.urls import path


class UserAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ['name', 'active']

class PhoneNumberFilter(admin.SimpleListFilter):
    title = 'Phone Number'
    parameter_name = 'phone_no'

    def lookups(self, request, model_admin):
        return (
            ('+9230', '+9230'),
            ('+9231', '+9231'),
            ('+9232', '+9232'),
            ('+9233', '+9233'),
            ('+9234', '+9234'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(phone_no__startswith=value)

    
class ProfileAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ['user', 'role', 'phone_no']

    def get_list_filter(self, request):
        return [PhoneNumberFilter]

    def fake_data(self, request):
       success = management.call_command("fake_user_profile")
       return HttpResponseRedirect("../")
      
    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path(
               "fake_data/",
               self.fake_data,
               name = 'fake_data'
           )
       ]
       return custom_urls + urls
   
class ProjectAdmin(admin.ModelAdmin):
    change_list_template = "admin/project_change_list.html"
    list_display = ['title', 'start_date', 'end_date']
    def fake_project(self, request):
       success = management.call_command("fake_project")
       return HttpResponseRedirect("../")
      
    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path(
               "fake_project/",
               self.fake_project,
               name = 'fake_project'
           )
       ]
       return custom_urls + urls
 
class TaskAdmin(admin.ModelAdmin):
    change_list_template = "admin/task_change_list.html"
    list_display = ['title', 'status', 'project']
    list_filter = ['status']
    def fake_task(self, request):
       success = management.call_command("fake_task")
       return HttpResponseRedirect("../")
      
    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path(
               "fake_task/",
               self.fake_task,
               name = 'fake_task'
           )
       ]
       return custom_urls + urls
class DocumentAdmin(admin.ModelAdmin):
    change_list_template = "admin/doc_change_list.html"
    list_display = ['name', 'version', 'project']
    def fake_doc(self, request):
       success = management.call_command("fake_doc")
       return HttpResponseRedirect("../")
      
    def get_urls(self):
       urls = super().get_urls()
       custom_urls = [
           path(
               "fake_doc/",
               self.fake_doc,
               name = 'fake_doc'
           )
       ]
       return custom_urls + urls
   
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Document, DocumentAdmin)
