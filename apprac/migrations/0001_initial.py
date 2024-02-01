# Generated by Django 5.0 on 2024-02-01 10:58

import apprac.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', apprac.models.PhoneField(max_length=13)),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('qa', 'Qa'), ('developer', 'Developer')], default='developer')),
                ('display_pic', models.ImageField(blank=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'user_table',
            },
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
                ('file', models.FileField(upload_to='file/')),
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
                'ordering': ['status'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apprac.user', verbose_name='User Profile'),
        ),
    ]
