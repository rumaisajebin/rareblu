# Generated by Django 4.2.6 on 2023-12-06 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0027_applied_coupon_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(default=None, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(default=None, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(default=None, null=True, upload_to='product'),
        ),
    ]
