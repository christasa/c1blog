# Generated by Django 2.1.5 on 2019-04-04 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chris', '0002_aboutme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutme',
            old_name='introduce',
            new_name='introduction',
        ),
    ]