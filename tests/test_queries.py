from ..query import check_if_feature_value_match


class TestQueries():
    def test_query_for_feature(self):
        example_data = [
            {
                "feature_1": 5,
                "feature_2": 6,
                "feature_3": "a"
            },
            {
                "feature_1": 2,
                "feature_2": 7,
            },
            {
                "feature_1": 5,
                "feature_2": 25,
                "feature_3": "a"
            },
        ]

        matching_query = check_if_feature_value_match(
            {
                "feature_3": "a", "feature_1": 5
            },
            example_data
        )
        expected_query = [
            {
                "feature_1": 5,
                "feature_2": 6,
                "feature_3": "a"
            },
            {
                "feature_1": 5,
                "feature_2": 25,
                "feature_3": "a"
            },
        ]
        assert matching_query == expected_query