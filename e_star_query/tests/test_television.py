from energy_star_database.e_star_query.datasets.television_data import Television
from energy_star_database.e_star_query.datasets.television_datasets import get_features, check_features


class TestTelevision():
    # def test_television(self):
    #     test_television = Television(**data_set[0])
    #     expected_size_inches = 42.51
    #     assert test_television.size_inches == expected_size_inches
    #
    #     dict_of_televisioon = vars(test_television)
    #
    #     assert dict_of_televisioon["size_inches"] == expected_size_inches

    def test_get_features(self):
        features = get_features("television")

    def test_get_features_uips(self):
        features = get_features("uninterruptible power supplies")

    def test_check_features(self):
        expected_features = {
            "size_inches": 42.51
        }
        actual = check_features("television",expected_features)
        expected =  {'pd_id': '2328272',
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
