# Generated by Django 3.2.7 on 2021-09-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0008_alter_userprofile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]