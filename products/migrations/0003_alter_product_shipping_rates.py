# Generated by Django 4.2.13 on 2024-05-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_price_product_product_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="shipping_rates",
            field=models.IntegerField(default=0),
        ),
    ]
