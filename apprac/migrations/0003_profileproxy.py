# Generated by Django 5.0 on 2024-02-28 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprac', '0002_rename_contact_no_profile_phone_no_and_more'),
    ]

    operations = [
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
    ]
