# Generated by Django 3.0.1 on 2020-01-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='createPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(upload_to='posts/posts_images/')),
                ('post_caption', models.TextField(max_length=140)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]