# Generated by Django 4.2.5 on 2023-11-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_number_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_news',
            field=models.IntegerField(max_length=100, null=True, verbose_name='id_news'),
        ),
    ]