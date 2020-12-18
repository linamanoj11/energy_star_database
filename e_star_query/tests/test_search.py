import csv

from energy_star_database.e_star_query.search.search import search


class TestSearch():
    def test_search_television(self):
        actual = search("television", {
            "size_inches": 65
        })
        assert len(actual) == 3

        with open("test.csv", "w") as csvfile:
            fieldnames = actual[0].keys()
            writer=csv.DictWriter(
                csvfile,
                fieldnames=fieldnames
            )
            writer.writeheader()
            for row in actual:
                writer.writerow(
                    row
                )
