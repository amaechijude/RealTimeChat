# Generated by Django 5.0.6 on 2024-07-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomchat',
            name='content',
            field=models.CharField(max_length=300),
        ),
    ]
