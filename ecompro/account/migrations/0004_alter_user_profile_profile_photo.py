# Generated by Django 4.2.6 on 2023-12-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='profile_photo',
            field=models.ImageField(default=None, null=True, upload_to='profile'),
        ),
    ]