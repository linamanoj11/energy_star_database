from energy_star_database.e_star_query.search.search import search


class TestSearch():
    def test_search_television(self):
        actual = search("television", {
            "size_inches": 65
        })
        assert len(actual) == 3