from ..datasets.energy_star_datasets import TelevisionDataset, \
    UninterruptiblePowerSuppliesDataset, ElectricVehicleSupplyDatasets


class TestEnergyStarDataSetGetFeatures():
    def test_television_dataset(self):
        television_data = TelevisionDataset()
        actual = television_data.get_product_features()
        expected_fourth_row_model_name = "E657Q"
        expected_fourth_row_delta_watts = 20.03

        assert actual[3]["model_name"] == expected_fourth_row_model_name
        assert round(actual[3]["delta_watts"],2) == expected_fourth_row_delta_watts

    def test_uips_dataset(self):
        television_data = UninterruptiblePowerSuppliesDataset()
        actual = television_data.get_product_features()
        expected_fourth_row_model_name = "0E-625V8LCD"
        expected_fourth_row_delta_watts = 1592.84

        assert actual[3]["model_name"] == expected_fourth_row_model_name
        assert round(actual[3]["delta_watts"],2) == expected_fourth_row_delta_watts

    def test_electric_vehicle_dataset(self):
        television_data = ElectricVehicleSupplyDatasets()
        actual = television_data.get_product_features()
        expected_fourth_row_model_name = "POWERPORT"
        expected_fourth_row_delta_watts = 22.36

        assert actual[3]["model_name"] == expected_fourth_row_model_name
        assert round(actual[3]["delta_watts"],2) == expected_fourth_row_delta_watts

    class TestCheckFeatures():
        def test_check_features(self):
            expected_features = {
                "size_inches": 42.51
            }
            actual = TelevisionDataset().check_features(expected_features)
            expected = {'pd_id': '2328272',
                        'brand_name': 'NEC',
                        'model_name': 'E437Q',
                        'model_number': 'E437Q',
                        'size_inches': 42.51,
                        'resolution_pixels': '3840x2160',
                        'power_consumption_in_on_mode_watts': 60.64,
                        'maximum_on_mode_power_for_certification_watts': 61.04,
                        'power_consumption_in_standby_mode_watts': 0.5,
                        'maximum_standby_passive_mode_power_for_certification_watts': 0.35,
                        'ethernet_supported': 'Fast Ethernet (100 Mbit/s)',
                        'technology_type': 'Direct-lit LED',
                        "delta_watts": 0.174}

            # TODO assert almost equal
            for key, value in actual[0].items():
                if key != "delta_watts":
                    assert value == expected[key]

