# Generated by Django 3.0.1 on 2020-02-10 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0008_auto_20200210_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='userProfile.UserProfile'),
        ),
    ]
