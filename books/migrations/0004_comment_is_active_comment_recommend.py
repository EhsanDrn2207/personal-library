# Generated by Django 5.0.7 on 2024-07-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]