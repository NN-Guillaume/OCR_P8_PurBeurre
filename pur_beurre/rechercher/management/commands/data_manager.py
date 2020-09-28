"""Classes for the application purbeurre"""

from django.core.management.base import BaseCommand
import requests
from homepage.models import *

CATEGORY = {
    1: "eaux",
    2: "bieres",
    3: "sodas",
    4: "snacks",
}


class GetProduct:
    """Class to create product objects"""

    def __init__(self, data, category):
        self.id_product = data["products"]["id"]
        self.product_name = data["products"]["product_name"]
        self.nutri_score = data["products"]["nutrition_grades"]
        self.ingredients = data["Products"]["ingredients_text_fr"] #will it works ?
        self.img_product = data["products"]["image_url"]
        self.where_to_buy = data["products"]["stores"]
        self.url = data["products"]["url"]
        self.categorie = category # ??????????

    def list_attributes(self):
        return (
            self.id_product,
            self.product_name,
            self.nutri_score,
            self.ingredients,
            self.img_product,
            self.where_to_buy,
            self.url,
            self.categorie,
        )


class GetCategory:
    """Class to create category objects"""

    def __init__(self, id, name):
        self.id_categorie = id
        self.categorie_name = name


class Database:
    """Insertion datas from OpenFoodFact in purbeurre's database"""

    def get_api_product(self, category_name, page_number):
        page = (
            "https://fr.openfoodfacts.org/categorie/"
            + category_name
            + "/"
            + str(page_number)
            + ".json"
        )
        r = requests.get(page)
        data = r.json()
        return data

    def insert_data(self, maximum):
        for value in CATEGORY.values():
            categorie = GetCategory(value)

            if not Categories.objects.filter(categorie_name=Categories.categorie_name).exists():
                Categories.objects.create(categorie_name=Categories.categorie_name)

            key = Categories.objects.get(categorie_name=Categories.categorie_name)

            total_products = 0
            page_number = 1
            while total_products < maximum:
                data = self.get_api_product(categorie.name, page_number)

                product_number = 0
                while (
                    product_number < len(data["products"]) and total_products < maximum
                ):
                    # verify quality of the data collected
                    # before insert it in local database
                    try:
                        product_object = GetProduct(data, product_number, key)
                        attributes = product_object.list_attributes()

                        for item in attributes:
                            assert len(str(item)) > 0
                    except KeyError:
                        pass
                    except AssertionError:
                        pass
                    else:
                        total_products += 1

                        if not Product.objects.filter(
                            code=product_object.code
                        ).exists():
                            Product.objects.create(
                                
                                name=product_object.product_name,
                                nutri_score=product_object.nutri_score,
                                ingredients=product_object.ingredients,
                                stores=product_object.where_to_buy,
                                link=product_object.url,
                                image=product_object.img_product,
                                id_categorie=product_object.categorie,
                            )
                    product_number += 1
                page_number += 1


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Updating database...")
        newData = Database()
        newData.insert_data(10)
        print("Done !")