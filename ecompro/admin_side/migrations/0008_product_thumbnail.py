# Generated by Django 4.2.6 on 2023-11-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=2, upload_to='product'),
            preserve_default=False,
        ),
    ]
