from energy_star_database.e_star_query.datasets.energy_star_datasets import TelevisionDataset
from energy_star_database.e_star_query.datasets.products.television_data import Television


class TestTelevision():
    def test_television(self):
        dataset = TelevisionDataset().get_data()
        test_television = Television(**dataset[0])
        expected_size_inches = 42.51
        assert test_television.size_inches == expected_size_inches

        dict_of_televisioon = vars(test_television)

        assert dict_of_televisioon["size_inches"] == expected_size_inches
