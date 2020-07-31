# Generated by Django 3.0.7 on 2020-07-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categorie', models.IntegerField(verbose_name='id_categorie')),
                ('categorie_name', models.CharField(max_length=200, unique=True, verbose_name='categorie_name')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_favorites', models.IntegerField(verbose_name='id_favorites')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField(verbose_name='id_product')),
                ('id_categorie', models.IntegerField(verbose_name='id_product')),
                ('product_name', models.CharField(max_length=100, unique=True, verbose_name='product_name')),
                ('nutri_score', models.CharField(max_length=1, verbose_name='nutri_score')),
                ('ingredients', models.CharField(max_length=300, verbose_name='ingredients')),
                ('img_product', models.URLField(verbose_name='img_product')),
                ('where_to_buy', models.CharField(max_length=300, verbose_name='where_to_buy')),
                ('url', models.CharField(max_length=300, unique=True, verbose_name='url')),
            ],
        ),
    ]
