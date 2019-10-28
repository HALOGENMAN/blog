# Generated by Django 2.2.4 on 2019-10-27 06:19

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_f', null=True, upload_to=post.models.upload_location, width_field='width_f')),
                ('width_f', models.IntegerField(default=0)),
                ('height_f', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestap', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestap', '-update'],
            },
        ),
    ]
