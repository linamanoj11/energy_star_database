#! /usr/bin/env python
import argparse
import csv

from .utils import get_product_from_category


# TODO test function
def _split_key_value_pairs(inputs):
    features = {}
    for input in inputs:
        key, value = input.split(":")
        features[key] = value
    return features


def search(product_category: str,
           known_features: dict):
    product = get_product_from_category(product_category)
    products_with_features = product.check_features(
        known_features
    )
    if len(products_with_features) == 0:
        print(f"No matching query for {known_features}")
        print(
            f"Check if features is a valid name this product {product_category} has the follwing features {list(product.get_data()[0].keys())}")
    return product.check_features(
        known_features
    )


# TODO test function
def write_csv(rows, product_category, csv_file_name=None):
    if csv_file_name is None:
        csv_file_name = f"energy_star_database_{product_category}.csv"
    with open(csv_file_name, "w") as csvfile:
        print(f"Writing to {csv_file_name}")
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


def main():
    parser = argparse.ArgumentParser(
        usage="Given a product category and the values of one or more features, "
              "output a CSV of all products that satisfy the search criteria"
    )
    parser.add_argument(
        "-product_category", type=str, required=True,
        help="Category for products to query from  EnergyStar database. Available product categories are "
             "['television', 'uninterruptible power supplies', and 'electric vehicle supply']"
    )

    parser.add_argument(
        "-features", required=True, nargs='*',
        help="Dictionary of feature keys and values used to narrow the search"
    )
    parser.add_argument(
        "-csv_name", type=str,
        help="name to write csv into. example: 'my_csv.csv' "
             "otherwise file will be saved into default filename given in output"
    )
    args = parser.parse_args()
    matching_rows = search(
        args.product_category,
        _split_key_value_pairs(args.features)
    )
    if len(matching_rows) > 0:

        write_csv(matching_rows, args.product_category, args.csv_name)
    else:
        print(f"Check feature arguement {args.features}")


if __name__ == '__main__':
    main()
