# Generated by Django 3.0.2 on 2020-02-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0014_auto_20200210_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='userProfile.UserProfile'),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]