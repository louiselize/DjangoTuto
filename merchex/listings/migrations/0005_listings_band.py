# Generated by Django 5.0.4 on 2024-04-24 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listings_description_listings_sold_listings_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]