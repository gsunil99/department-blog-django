# Generated by Django 3.1.4 on 2021-01-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=460),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post-default.jpg', upload_to='blog/post'),
        ),
    ]