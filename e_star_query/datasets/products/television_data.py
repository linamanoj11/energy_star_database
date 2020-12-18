from typing import Optional

from energy_star_database.e_star_query.datasets.products.product_class import ProductClass
from energy_star_database.e_star_query.datasets.utils import get_float_value


def delta_watts(size_inches, maximum_standby_passive_mode_power_for_certification_watts,
                power_consumption_in_standby_mode_watts, maximum_on_mode_power_for_certification_watts,
                power_consumption_in_on_mode_watts):
    if any(
            [size_inches is None,
             maximum_standby_passive_mode_power_for_certification_watts is None,
             power_consumption_in_standby_mode_watts is None,
             maximum_on_mode_power_for_certification_watts is None,
             power_consumption_in_on_mode_watts is None
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

    scaling_factor = _scaling_factor_from_size(size_inches)
    return scaling_factor * (
            (maximum_standby_passive_mode_power_for_certification_watts - power_consumption_in_standby_mode_watts)
            + (maximum_on_mode_power_for_certification_watts - power_consumption_in_on_mode_watts)
    )


class Television(ProductClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.technology_type: Optional[str] = kwargs.get('technology_type')
        self.ethernet_supported: Optional[str] = kwargs['ethernet_supported']
        self.size_inches: Optional[float] = get_float_value(kwargs, 'size_inches')
        self.resolution_pixels: Optional[str] = kwargs['resolution_pixels']
        self.power_consumption_in_on_mode_watts: Optional[float] = get_float_value(kwargs,
                                                                                   'power_consumption_in_on_mode_watts')
        self.maximum_on_mode_power_for_certification_watts: Optional[float] = get_float_value(kwargs,
                                                                                              'maximum_on_mode_power_for_certification_watts')
        self.power_consumption_in_standby_mode_watts: Optional[float] = get_float_value(kwargs,
                                                                                        'power_consumption_in_standby_mode_watts')
        self.maximum_standby_passive_mode_power_for_certification_watts: Optional[float] = get_float_value(kwargs,
                                                                                                           'maximum_standby_passive_mode_power_for_certification_watts')
        self.delta_watts: Optional[float] = delta_watts(
            self.size_inches, self.maximum_standby_passive_mode_power_for_certification_watts,
            self.power_consumption_in_standby_mode_watts, self.maximum_on_mode_power_for_certification_watts,
            self.power_consumption_in_on_mode_watts
        )
