# Generated by Django 2.2.4 on 2019-10-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestap',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
