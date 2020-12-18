from energy_star_database.e_star_query.utils import get_product_from_category


def get(product_category:str, brand_name:str, model_name:str):
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
    print(matching_rows[0])
    return matching_rows[0]