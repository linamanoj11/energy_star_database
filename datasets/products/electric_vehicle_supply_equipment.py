from ...datasets.products.product_class import ProductClass
from ...datasets.utils import get_float_value


class ElectricVehicleSupply(ProductClass):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_nameplate_output_current_a = get_float_value(kwargs, 'max_nameplate_output_current_a')
        self.input_voltage_v = get_float_value(kwargs, 'input_voltage_v')
        self.no_vehicle_mode_input_power_w = get_float_value(kwargs, 'no_vehicle_mode_input_power_w')
        self.no_vehicle_mode_total_allowance_w = get_float_value(kwargs, 'no_vehicle_mode_total_allowance_w')
        self.no_vehicle_mode_power_factor = get_float_value(kwargs, 'no_vehicle_mode_power_factor')
        self.partial_on_mode_input_power_w = get_float_value(kwargs, 'partial_on_mode_input_power_w')
        self.partial_on_mode_total_allowance_w = get_float_value(kwargs, 'partial_on_mode_total_allowance_w')
        self.partial_on_mode_power_factor = get_float_value(kwargs, 'partial_on_mode_power_factor')
        self.idle_mode_input_power_w = get_float_value(kwargs, 'idle_mode_input_power_w')
        self.idle_mode_total_allowance_w = get_float_value(kwargs, 'idle_mode_total_allowance_w')
        self.idle_mode_power_factor = get_float_value(kwargs, 'idle_mode_power_factor')
        self.full_current_operation_mode_test_total_loss_w = get_float_value(kwargs,
                                                                             'full_current_operation_mode_test_total_loss_w')
        self.delta_watts = self.calculate_delta_watts()

    def calculate_delta_watts(self):
        if any(
                [self.full_current_operation_mode_test_total_loss_w is None,
                 self.no_vehicle_mode_total_allowance_w is None,
                 self.no_vehicle_mode_input_power_w is None,
                 self.no_vehicle_mode_power_factor is None,
                 self.partial_on_mode_total_allowance_w is None,
                 self.partial_on_mode_input_power_w is None,
                 self.partial_on_mode_power_factor is None,
                 self.idle_mode_total_allowance_w is None,
                 self.idle_mode_input_power_w is None,
                 self.idle_mode_power_factor is None]
        ):
            return None
        return self.full_current_operation_mode_test_total_loss_w \
               + ((
                              self.no_vehicle_mode_total_allowance_w - self.no_vehicle_mode_input_power_w) * self.no_vehicle_mode_power_factor) \
               + ((
                              self.partial_on_mode_total_allowance_w - self.partial_on_mode_input_power_w) * self.partial_on_mode_power_factor) \
               + ((self.idle_mode_total_allowance_w - self.idle_mode_input_power_w) * self.idle_mode_power_factor)
