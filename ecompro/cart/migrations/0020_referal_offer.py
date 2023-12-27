# Generated by Django 4.2.6 on 2023-12-16 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0019_order_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referal_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_code', models.CharField(max_length=20, unique=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('referred_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
