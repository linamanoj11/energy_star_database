from .datasets.energy_star_datasets import TelevisionDataset, \
    UninterruptiblePowerSuppliesDataset, ElectricVehicleSupplyDatasets

TELEVISION_STRINGS = [
    "television", "Television", "television".upper()
]
UINTERRUPTIPLE_POWER_SUPPLIES_STRINGS = [
    "uninterruptible power supplies", "uninterruptible_power_supplies",
    "uninterruptible power supplies".upper(),"Uninterruptible Power Supplies",
"uninterruptible_power_supplies".upper()
]

ELECTRIC_VEHICLE_SUPPLY_STRINGS = [
    "electric vehicle supply", "electric_vehicle_supply",
    "electric vehicle supply".upper(), "electric_vehicle_supply".upper(), "Electric Vehicle Supply"
    "electric_vehicle_chargers", "electric vehicle chargers", "electric vehicle chargers".upper(),
    "electric_vehicle_chargers".upper(), "Electric Vehicle Chargers",
]

def get_product_from_category(product_category:str):
    if product_category in TELEVISION_STRINGS:
        product = TelevisionDataset()
    elif product_category in UINTERRUPTIPLE_POWER_SUPPLIES_STRINGS:
        product = UninterruptiblePowerSuppliesDataset()
    elif product_category in ELECTRIC_VEHICLE_SUPPLY_STRINGS:
        product = ElectricVehicleSupplyDatasets()
    else:
        raise ValueError(
            f"{product_category} is not a valid product category"
        )
    return product