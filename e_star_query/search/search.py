import csv

from energy_star_database.e_star_query.utils import get_product_from_category


def search(product_category:str,
           known_features: dict):
    product = get_product_from_category(product_category)
    return product.check_features(
        known_features
    )
