from enum import Enum

from energy_star_database.e_star_query.datasets.energy_star_datasets import SOCRATA_CLIENT
from energy_star_database.e_star_query.datasets.television_data import Television
from energy_star_database.e_star_query.datasets.uninterruptible_power_supplies import UninterruptiblePowerSupplies
from energy_star_database.e_star_query.query import check_if_feature_value_match

TELEVISION_ID = "vd8s-5tty"
UNINTERRUPTIBLEPOWERSUPPLIES_ID = "ifxy-2uty"
ELECTRIC_VEHICILE_SUPPLY_EQUIPMENT_ID = "y2tt-wp6c"

# TODO use classes to break this apart

class Product(Enum):
    TELEVISION = "television"
    UNINTERRUPTIBLEPOWERSUPPLIES = "uninterruptible power supplies"
    ELECTRIC_VEHICILE_SUPPLY_EQUIPMENT = "ElectricVehicle Supply Equipment"


def get_features(product_category_input:str):
    product_category = Product(product_category_input)
    product_features = []
    if product_category == Product.TELEVISION:
        data_set = SOCRATA_CLIENT.get(TELEVISION_ID)
    elif product_category == Product.ELECTRIC_VEHICILE_SUPPLY_EQUIPMENT:
        data_set = SOCRATA_CLIENT.get(ELECTRIC_VEHICILE_SUPPLY_EQUIPMENT_ID)
    elif product_category == Product.UNINTERRUPTIBLEPOWERSUPPLIES:
        data_set = SOCRATA_CLIENT.get(UNINTERRUPTIBLEPOWERSUPPLIES_ID)
    else:
        return(print(f'{product_category_input} is not a product category'))
    for data_row in data_set:
        if product_category == Product.TELEVISION:
            product = Television(**data_row)
        if product_category == Product.UNINTERRUPTIBLEPOWERSUPPLIES:
            product = UninterruptiblePowerSupplies(**data_row)
        product_feature = vars(product)
        product_features.append(product_feature)
    return product_features


def check_features(product_category_input:str, expected_features:dict):
    features = get_features(product_category_input)
    return check_if_feature_value_match(expected_features,features)
