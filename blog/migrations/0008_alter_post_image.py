# Generated by Django 4.2.2 on 2023-07-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='postimg_def.jpg', upload_to='Posts_pics/%y/%m/%d'),
        ),
    ]
