# Generated by Django 4.2.5 on 2023-11-23 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_number_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='number_news',
        ),
    ]
