# Generated by Django 5.1.2 on 2024-11-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
