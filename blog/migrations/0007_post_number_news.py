# Generated by Django 4.2.5 on 2023-11-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_news',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
