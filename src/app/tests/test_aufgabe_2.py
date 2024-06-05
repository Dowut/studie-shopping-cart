import unittest

from src.app.routes.admin import get_dynamic_table
from src.app.routes.user import profile_home_blueprint


class TestOrderTable(unittest.TestCase):

    # TODO Codequalität anpassen
    def test_new_feature(self):
        test_input = []
        self.assertIsNotNone(test_input)

        # test_input NICHT anpassen
        test_input = [
            [1, 12, "B: Test Product"],
            [2, 12, "B: Test Product"],
            [3, 12, "B: Test Product"],
            [4, 1, "A: Test Product"],
            [5, 1, "A: Test Product"],
            [6, 12, "Z: Test Product"]
        ]

        # TODO Codequalität in Methode anpassen in ./src/app/routes/admin.py
        dynamic_table = get_dynamic_table(test_input)

        # TODO expected_outcome anpassen um Test zu fixen: D.h. prüfen, was die Methode für den oberen test_input
        #  get_dynamic_table zurückgibt und hier entsprechend anpassen.
        expected_outcome = [
            ["Order ID", "B: Test Product", "A: Test Product", "Z: Test Product"],
            [12, 0, 3, 1],
            [1, 2, 0, 0],
        ]

        # Testet, ob expected_outcome gleich dem return Wert der Methode get_dynamic_table ist
        self.assertTrue(expected_outcome == dynamic_table)


if __name__ == '__main__':
    unittest.main()
