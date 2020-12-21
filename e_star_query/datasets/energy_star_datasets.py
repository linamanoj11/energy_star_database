from abc import ABC, abstractmethod

from sodapy import Socrata


from ..datasets.products.electric_vehicle_supply_equipment import ElectricVehicleSupply
from ..datasets.products.television_data import Television
from ..datasets.products.uninterruptible_power_supplies import \
    UninterruptiblePowerSupplies
from ..query import check_if_feature_value_match

SOCRATA_DOMAN = 'data.energystar.gov'
TOKEN_TEXT = "z7rbgOa4tVyiRSpwMQDF4xrv6"


class EnergyStarDatasets(ABC):
    def __init__(self):
        self.id = "Fake"
        self.domain='data.energystar.gov'
        self.token_text = "z7rbgOa4tVyiRSpwMQDF4xrv6"
        self.client = Socrata(self.domain, self.token_text)

    def get_data(self):
        return self.client.get(self.id)

    @abstractmethod
    def get_product_features(self)->list:
        pass

    def check_features(self,expected_features:dict):
        return check_if_feature_value_match(expected_features, self.get_product_features())


class TelevisionDataset(EnergyStarDatasets):
    def __init__(self):
        super().__init__()
        self.id = "vd8s-5tty"

    def get_product_features(self):
        return [
            vars(Television(**data_row)) for data_row in self.get_data()
        ]


class UninterruptiblePowerSuppliesDataset(EnergyStarDatasets):
    def __init__(self):
        super().__init__()
        self.id = "ifxy-2uty"

    def get_product_features(self):
        return [
            vars(UninterruptiblePowerSupplies(**data_row)) for data_row in self.get_data()
        ]


class ElectricVehicleSupplyDatasets(EnergyStarDatasets):
    def __init__(self):
        super().__init__()
        self.id = "y2tt-wp6c"

    def get_product_features(self):
        return [
            vars(ElectricVehicleSupply(**data_row)) for data_row in self.get_data()
        ]