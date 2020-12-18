import csv

from energy_star_database.e_star_query.utils import get_product_from_category


def search(product_category:str,
           known_features: dict):
    product = get_product_from_category(product_category)
    return product.check_features(
        known_features
    )


def write_csv(rows):
    with open("test.csv", "w") as csvfile:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                row
            )