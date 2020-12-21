from ...datasets.products.product_class import ProductClass
from ...datasets.utils import get_float_value

pct_time_at_0_load=0.8
pct_time_at_25_load=0.1
pct_time_at_50_load=0.02
pct_time_at_75_load=0.03
pct_time_at_100_load=0.05

def delta_watts(
total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac,
efficiency_at_25_load_min_config_lowest_dependency_ac,
efficiency_at_50_load_min_config_lowest_dependency_ac,
efficiency_at_75_load_min_config_lowest_dependency_ac,
efficiency_at_100_load_min_config_lowest_dependency_ac,
):
    if any(
            [total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac is None,
             efficiency_at_25_load_min_config_lowest_dependency_ac is None,
             efficiency_at_50_load_min_config_lowest_dependency_ac is None,
             efficiency_at_75_load_min_config_lowest_dependency_ac is None,
             efficiency_at_100_load_min_config_lowest_dependency_ac is None
             ]
    ):
        return None
    return total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac *(
            (pct_time_at_0_load * 1.0)
            + (pct_time_at_25_load * efficiency_at_25_load_min_config_lowest_dependency_ac)
            + (pct_time_at_50_load * efficiency_at_50_load_min_config_lowest_dependency_ac)
            + (pct_time_at_75_load * efficiency_at_75_load_min_config_lowest_dependency_ac)
            + (pct_time_at_100_load * efficiency_at_100_load_min_config_lowest_dependency_ac)
    )


class UninterruptiblePowerSupplies(ProductClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_output_power_rating_minimum_configuration_w = get_float_value(kwargs, 'active_output_power_rating_minimum_configuration_w')
        self.height_mm = get_float_value(kwargs, 'height_mm')
        self.width_mm = get_float_value(kwargs, 'width_mm')
        self.depth_mm = get_float_value(kwargs, 'depth_mm')
        self.topology_ac = get_float_value(kwargs, 'height_mm')
        self.total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac = get_float_value(kwargs, 'height_mm')
        self.efficiency_at_25_load_min_config_lowest_dependency_ac = get_float_value(kwargs, 'efficiency_at_25_load_min_config_lowest_dependency_ac')
        self.efficiency_at_50_load_min_config_lowest_dependency_ac = get_float_value(kwargs, 'efficiency_at_50_load_min_config_lowest_dependency_ac')
        self.efficiency_at_75_load_min_config_lowest_dependency_ac = get_float_value(kwargs, 'efficiency_at_75_load_min_config_lowest_dependency_ac')
        self.efficiency_at_100_load_min_config_lowest_dependency_ac = get_float_value(kwargs, 'efficiency_at_100_load_min_config_lowest_dependency_ac')
        self.delta_watts = delta_watts(
            self.total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac,
            self.efficiency_at_25_load_min_config_lowest_dependency_ac,
            self.efficiency_at_50_load_min_config_lowest_dependency_ac,
            self.efficiency_at_75_load_min_config_lowest_dependency_ac,
            self.efficiency_at_100_load_min_config_lowest_dependency_ac,
        )