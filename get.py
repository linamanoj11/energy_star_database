#! /usr/bin/env python
import argparse

from .utils import get_product_from_category


def get(product_category: str, brand_name: str, model_name: str):
    product = get_product_from_category(product_category)
    matching_rows = product.check_features(
        {
            "brand_name": brand_name, "model_name": model_name
        }
    )
    if len(matching_rows) < 0:
        return None
    elif len(matching_rows) > 1:
        print("More then 1 result matches query please use search for more infor")
    return matching_rows[0]


def main():
    parser = argparse.ArgumentParser(usage="Given a product category, brand name, and model name, "
                                           "fetch the product info from the EnergyStar database")
    parser.add_argument(
        "-product_category", type=str, required=True,
        help="Category for products to query from  EnergyStar database. Available product categories are "
             "['television', 'uninterruptible power supplies', and 'electric vehicle supply']"
    )
    parser.add_argument(
        "-brand_name", type=str, required=True, help="brand name for a particular product category"
    )
    parser.add_argument(
        "-model_name", type=str, required=True, help="model name for a particular product category"
    )
    args = parser.parse_args()
    print(get(args.product_category, args.brand_name, args.model_name))


if __name__ == '__main__':
    main()
