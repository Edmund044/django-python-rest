# Generated by Django 4.2.13 on 2024-05-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="product_description",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="product_image",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="reviews",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="product",
            name="shipping_rates",
            field=models.IntegerField(default=0, max_length=255),
        ),
    ]
