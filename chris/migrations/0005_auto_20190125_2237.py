# Generated by Django 2.1.5 on 2019-01-25 14:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chris', '0004_auto_20190125_1847'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='UserFile',
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
