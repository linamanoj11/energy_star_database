def delta_watts(size_inches, maximum_standby_passive_mode_power_for_certification_watts,
                power_consumption_in_standby_mode_watts, maximum_on_mode_power_for_certification_watts,
                power_consumption_in_on_mode_watts):
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


class Television():
    def __init__(self, **kwargs):
        self.pd_id:str = kwargs['pd_id']
        self.brand_name:str= kwargs['brand_name']
        self.model_name:str=kwargs['model_name']
        self.technology_type:str=kwargs['technology_type']
        self.ethernet_supported:str=kwargs['ethernet_supported']
        self.size_inches:float=float(kwargs['size_inches'])
        self.resolution_pixels:str=kwargs['resolution_pixels']
        self.power_consumption_in_on_mode_watts:float=float(kwargs['power_consumption_in_on_mode_watts'])
        self.maximum_on_mode_power_for_certification_watts:float=float(kwargs['maximum_on_mode_power_for_certification_watts'])
        self.power_consumption_in_standby_mode_watts:float=float(kwargs['power_consumption_in_standby_mode_watts'])
        self.maximum_standby_passive_mode_power_for_certification_watts:float=float(kwargs['maximum_standby_passive_mode_power_for_certification_watts'])
        self.delta_watts:float = delta_watts(
            self.size_inches, self.maximum_standby_passive_mode_power_for_certification_watts,
            self.power_consumption_in_standby_mode_watts, self.maximum_on_mode_power_for_certification_watts,
            self.power_consumption_in_on_mode_watts
        )
