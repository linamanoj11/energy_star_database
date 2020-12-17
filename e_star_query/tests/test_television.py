from sodapy import Socrata

from energy_star_database.e_star_query.datasets.television import Television

television_id = "vd8s-5tty"
socrata_domain = 'data.energystar.gov'
token_text = "z7rbgOa4tVyiRSpwMQDF4xrv6"

class TestTelevision():
    def test_television(self):
        client = Socrata(socrata_domain, token_text)
        list_of_data = client.get(television_id)
        test_television = Television(**list_of_data[0])
        expected_size_inches = 42.51
        assert test_television.size_inches == expected_size_inches

        dict_of_televisioon = vars(test_television)

        assert dict_of_televisioon["size_inches"] == expected_size_inches