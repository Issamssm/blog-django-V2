# Generated by Django 4.2.2 on 2023-07-23 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categry',
        ),
    ]
