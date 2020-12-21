from ..get import get


class TestGet():
    def test_get_telvision(self):
        actual = get(
          "television",
            "Silo",
            "SL6520V12"
        )
        expected_pd_id = "2366117"

        assert actual["pd_id"] == expected_pd_id

    def test_get_uips(self):
        actual = get(
          "uninterruptible power supplies",
            "EATON",
            "9PX2200GRT"
        )
        expected_pd_id = "2331037"

        assert actual["pd_id"] == expected_pd_id

    def test_get_electric_vehicle_supply(self):
        actual = get(
          "electric vehicle supply",
            "ChargePoint",
            "CPH12"
        )
        expected_pd_id = "2293176"

        assert actual["pd_id"] == expected_pd_id