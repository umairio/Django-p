from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.utils import timezone
import re
from django.utils.translation import gettext as _




class User(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    
    class Meta:
        db_table = 'user_table'
        
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    class Role(models.TextChoices):
        Manager  = 'manager'
        QA = 'qa'
        Developer = 'developer'
        
    user = models.OneToOneField(User, verbose_name=("User Profile"), on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    role = models.CharField(choices = Role.choices, default = Role.Developer)
    display_pic = models.ImageField(upload_to='image/', blank=True)
    
    @property
    def full_name(self):
        return f'{self.user.name} - {self.role}'
    
    def __str__(self):
        return self.full_name
    
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    team_member = models.ManyToManyField(Profile, verbose_name=("Team Member"))
    
    class Meta:
        ordering = ['project', 'status']
        
    def __str__(self):
        return self.title
    

class Task(models.Model):
    class Status(models.TextChoices):
        Open  = 'Open'
        Review = 'Review'
        Working = 'Working'
        Awaiting_release = 'Awaiting_release'
        Waiting_qa = 'Waiting_qa'
        
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.CharField(choices = Status.choices, default = Status.Open)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ManyToManyField(Profile)
    
    @classmethod
    def get_qa_tasks(cls):
        return cls.objects.filter(status=Task.Status.Waiting_qa)
    
    @staticmethod
    def is_valid_status(status):
        return status in [Task.Status.Open, Task.Status.Review, Task.Status.Working]
    
    class Meta:
        ordering = ['status']
    
    def __str__(self):
        return self.title
    
class VersionField(models.Field):
                   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_prep_value(self, value):
        return str(value)
    
    def db_type(self, connection):
        return f"char({13})"
    
    def validate(self, value, model_instance):
        """Check if value consists only of valid emails."""
        super().validate(value, model_instance)
        ver_pattern = re.compile(r'^[vV]+[0-9-]+\.[0-9-]+\.[0-9-]+[a-zA-Z]$')
        match = ver_pattern.match(value)
        if not bool(match):
            raise ValidationError(
                _(
                    'Invalid version format. It should start with "v" or "V" followed by three numerical segments Year,Month,Patchc'
                    'separated by dots, and ending with a single alphabetical segment. Example: "v2024.12.3a"'
                ),
                code="invalid",
                params={"value": value},
            )
        
fields.VersionField = VersionField
   
class Document(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='file/', max_length=100)
    version = VersionField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
