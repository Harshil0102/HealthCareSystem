# Generated by Django 4.1.7 on 2023-04-29 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_service',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.service'),
        ),
    ]
