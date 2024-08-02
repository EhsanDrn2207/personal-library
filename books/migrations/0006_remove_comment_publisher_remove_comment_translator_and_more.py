# Generated by Django 5.0.7 on 2024-08-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comment_publisher_comment_translator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='translator',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]