# Generated by Django 5.0 on 2024-01-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprac', '0002_alter_comment_author_alter_project_team_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='display_pic',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]
