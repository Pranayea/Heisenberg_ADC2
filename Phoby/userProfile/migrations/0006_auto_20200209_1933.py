# Generated by Django 3.0.2 on 2020-02-10 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0005_merge_20200209_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='userProfile.UserProfile'),
        ),
    ]