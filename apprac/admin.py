from django.contrib import admin
from django.core import management
from django.http import HttpResponseRedirect
from django.urls import path

from .models import Document, Profile, ProfileProxy, Project, Task, User


class UserAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ["name", "active"]
    search_fields = ("name", "active")


class PhoneNumberFilter(admin.SimpleListFilter):
    title = "Phone Number"
    parameter_name = "phone_no"

    def lookups(self, request, model_admin):
        return (
            ("+9230", "+9230"),
            ("+9231", "+9231"),
            ("+9232", "+9232"),
            ("+9233", "+9233"),
            ("+9234", "+9234"),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(phone_no__startswith=value)


admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    change_list_template = "admin/profile_change_list.html"
    list_display = ["user", "role", "phone_no"]
    search_fields = ("user__name", "role", "phone_no")

    def get_list_filter(self, request):
        return [PhoneNumberFilter]

    def fake_data(self, request):
        management.call_command("fake_user_profile")
        return HttpResponseRedirect("../")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("fake_data/", self.fake_data, name="fake_data")]
        return custom_urls + urls


admin.site.register(Profile, ProfileAdmin)


class ProjectAdmin(admin.ModelAdmin):
    change_list_template = "admin/project_change_list.html"
    list_display = ["title", "start_date", "end_date"]
    search_fields = ("title", "start_date", "end_date")

    def fake_project(self, request):
        management.call_command("fake_project")
        return HttpResponseRedirect("../")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("fake_project/", self.fake_project, name="fake_project")]
        return custom_urls + urls


admin.site.register(Project, ProjectAdmin)


class TaskAdmin(admin.ModelAdmin):
    change_list_template = "admin/task_change_list.html"
    list_display = ["title", "status", "project"]
    search_fields = ("title", "status")
    list_filter = ["status"]

    def fake_task(self, request):
        management.call_command("fake_task")
        return HttpResponseRedirect("../")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("fake_task/", self.fake_task, name="fake_task")]
        return custom_urls + urls


admin.site.register(Task, TaskAdmin)


class DocumentAdmin(admin.ModelAdmin):
    change_list_template = "admin/doc_change_list.html"
    list_display = ["name", "version", "project"]
    search_fields = ("name", "version")

    def fake_doc(self, request):
        management.call_command("fake_doc")
        return HttpResponseRedirect("../")

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("fake_doc/", self.fake_doc, name="fake_doc")]
        return custom_urls + urls


admin.site.register(Document, DocumentAdmin)


@admin.register(ProfileProxy)
class ProfileProxyAdmin(admin.ModelAdmin):

    list_display = ("full_name", "is_member_of_project", "is_assigned_to_task")
    search_fields = ("user__name", "role")
