# Generated by Django 5.0.6 on 2024-07-17 16:29

import django_resized.forms
import shortuuidfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='id',
        ),
        migrations.AddField(
            model_name='message',
            name='mID',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='room',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=70, scale=None, size=[1920, 1080], upload_to='media/room'),
        ),
    ]