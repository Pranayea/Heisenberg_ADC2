# Generated by Django 3.0.1 on 2020-02-09 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_of',
        ),
    ]
