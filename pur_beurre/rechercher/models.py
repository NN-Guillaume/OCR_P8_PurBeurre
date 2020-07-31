from django.db import models

# Create your models here.
class Categories(models.Model):
    id_categorie = models.IntegerField('id_categorie', null=False) #PK
    categorie_name = models.CharField('categorie_name', max_length=200, unique=True)

class Products(models.Model):
    id_product = models.IntegerField('id_product', null=False) #PK
    id_categorie = models.IntegerField('id_product', null=False) #FK
    product_name = models.CharField('product_name', null=False, max_length=100, unique=True)
    nutri_score = models.CharField('nutri_score', null=False, max_length=1)
    ingredients = models.CharField('ingredients', null=False, max_length=300)
    img_product= models.URLField('img_product',)
    where_to_buy = models.CharField('where_to_buy', max_length=300)
    url = models.CharField('url', null=False, max_length=300, unique=True)


class Favorites(models.Model):
    id_favorites = models.IntegerField('id_favorites', null=False) #PFK
    
