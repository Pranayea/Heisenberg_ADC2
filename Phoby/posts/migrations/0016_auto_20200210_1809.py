# Generated by Django 3.0.1 on 2020-02-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200210_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment_by',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='createposts',
            name='comment',
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.CreatePosts'),
        ),
    ]
