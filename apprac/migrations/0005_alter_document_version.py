# Generated by Django 5.0 on 2024-01-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprac', '0004_alter_document_description_alter_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='version',
            field=models.CharField(max_length=50),
        ),
    ]
