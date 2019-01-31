# Generated by Django 2.1.5 on 2019-01-31 10:18

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_contant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('abstract', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('url', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.AddField(
            model_name='blog_contant',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chris.BlogType'),
        ),
    ]
