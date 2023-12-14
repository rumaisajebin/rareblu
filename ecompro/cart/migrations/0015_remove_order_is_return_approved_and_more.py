# Generated by Django 4.2.6 on 2023-12-06 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0014_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_return_approved',
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_return_requested',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Order Confirmed'), ('shipped', 'Shipped'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered'), ('cancelled', 'cancelled'), ('returned', 'returned')], default='confirmed', max_length=20),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('balance_type', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit')], default='Credit', max_length=15)),
                ('balance_returned', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Returnedproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('return_status', models.CharField(choices=[('Return Pending', 'Return Pending'), ('Returned', 'Returned'), ('Rejected', 'Rejected')], default='Return Pending', max_length=20)),
                ('returned_at', models.DateTimeField(auto_now_add=True)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='returned_products', to='cart.order')),
            ],
        ),
    ]