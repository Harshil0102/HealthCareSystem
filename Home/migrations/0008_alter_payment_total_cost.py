# Generated by Django 4.1.7 on 2023-05-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_payment_total_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
