# Generated by Django 3.1.4 on 2021-02-01 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Catégorie',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('generic_name', models.CharField(max_length=300)),
                ('code_prod', models.CharField(max_length=50, unique=True)),
                ('brand_name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('nova_gps', models.PositiveSmallIntegerField()),
                ('nutri_grades', models.CharField(max_length=1)),
                ('pnns_gps1', models.CharField(max_length=200)),
                ('pnns_gps2', models.CharField(max_length=200)),
                ('store_name', models.CharField(max_length=200)),
                ('picture', models.URLField()),
                ('fat_100g', models.FloatField()),
                ('saturated_fat_100g', models.FloatField()),
                ('salt_100g', models.FloatField()),
                ('sugars_100g', models.FloatField()),
                ('categories', models.ManyToManyField(related_name='products', to='catalogue.Category')),
            ],
            options={
                'verbose_name': 'Produit',
            },
        ),
        migrations.CreateModel(
            name='FavoriteProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chosen_product', to='catalogue.product')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='healthy_substitute', to='catalogue.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favoris',
                'unique_together': {('product_id', 'substitute_id')},
            },
        ),
    ]
