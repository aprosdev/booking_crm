# Generated by Django 4.2.2 on 2023-07-16 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_invoice_total_for_single_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='grand_total',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='vat',
        ),
    ]
