# Generated by Django 3.0.1 on 2020-01-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('hobby_id', models.AutoField(primary_key=True, serialize=False)),
                ('hobby_name', models.CharField(max_length=15)),
                ('followers', models.IntegerField()),
                ('posts', models.IntegerField()),
            ],
        ),
    ]