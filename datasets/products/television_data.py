from typing import Optional

from ...datasets.products.product_class import ProductClass
from ...datasets.utils import get_float_value


class Television(ProductClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.technology_type = kwargs.get('technology_type')
        self.ethernet_supported = kwargs['ethernet_supported']
        self.size_inches = get_float_value(kwargs, 'size_inches')
        self.resolution_pixels = kwargs['resolution_pixels']
        self.power_consumption_in_on_mode_watts = get_float_value(kwargs,
                                                                  'power_consumption_in_on_mode_watts')
        self.maximum_on_mode_power_for_certification_watts = get_float_value(kwargs,
                                                                             'maximum_on_mode_power_for_certification_watts')
        self.power_consumption_in_standby_mode_watts = get_float_value(kwargs,
                                                                       'power_consumption_in_standby_mode_watts')
        self.maximum_standby_passive_mode_power_for_certification_watts = get_float_value(kwargs,
                                                                                          'maximum_standby_passive_mode_power_for_certification_watts')
        self.delta_watts = self.calculate_delta_watts()

    def calculate_delta_watts(self):
        if any(
                [self.size_inches is None,
                 self.maximum_standby_passive_mode_power_for_certification_watts is None,
                 self.power_consumption_in_standby_mode_watts is None,
                 self.maximum_on_mode_power_for_certification_watts is None,
                 self.power_consumption_in_on_mode_watts is None
                 ]
        ):
            return None

        def _scaling_factor_from_size(size_inches):
            if size_inches < 20:
                return 0.9
            elif size_inches < 40:
                return 0.85
            elif size_inches < 60:
                return 0.7
            else:
                return 0.65

        scaling_factor = _scaling_factor_from_size(self.size_inches)
        return scaling_factor * (
                (
                        self.maximum_standby_passive_mode_power_for_certification_watts - self.power_consumption_in_standby_mode_watts)
                + (self.maximum_on_mode_power_for_certification_watts - self.power_consumption_in_on_mode_watts)
        )
