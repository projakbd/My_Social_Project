# Generated by Django 3.2.7 on 2021-09-04 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_rename_user_userprofile_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='users',
            new_name='user',
        ),
    ]
