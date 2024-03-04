# Generated by Django 5.0 on 2024-03-04 10:53

import apprac.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', apprac.models.PhoneField(blank=True, max_length=13)),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('qa', 'Qa'), ('developer', 'Developer')], default='developer')),
                ('display_pic', models.ImageField(blank=True, upload_to='image/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apprac.profile',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
                ('team_member', models.ManyToManyField(to='apprac.profile', verbose_name='Team Member')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='file/')),
                ('version', apprac.models.VersionField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Review', 'Review'), ('Working', 'Working'), ('Awaiting_release', 'Awaiting Release'), ('Waiting_qa', 'Waiting Qa')], default='Open')),
                ('assignee', models.ManyToManyField(to='apprac.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.project')),
            ],
            options={
                'ordering': ['project', 'status'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.task')),
            ],
        ),
    ]
