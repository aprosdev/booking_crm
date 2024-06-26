# Generated by Django 4.2.2 on 2023-08-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_worker_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='site_contact',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr.'), ('Mrs', 'Mrs.'), ('Miss', 'Miss.')], max_length=5, null=True),
        ),
    ]
