# Generated by Django 3.0.2 on 2020-02-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_createposts_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createposts',
            name='uploaded_by',
        ),
    ]
