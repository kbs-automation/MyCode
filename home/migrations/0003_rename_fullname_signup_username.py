# Generated by Django 5.0.3 on 2024-03-11 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_signup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='fullname',
            new_name='username',
        ),
    ]
