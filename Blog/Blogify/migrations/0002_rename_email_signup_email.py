# Generated by Django 4.0.6 on 2022-11-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Email',
            new_name='email',
        ),
    ]
