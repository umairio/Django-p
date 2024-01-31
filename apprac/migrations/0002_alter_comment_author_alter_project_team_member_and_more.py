# Generated by Django 5.0 on 2024-01-31 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apprac.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team_member',
            field=models.ManyToManyField(to='apprac.profile', verbose_name='Team Member'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(to='apprac.profile'),
        ),
    ]
