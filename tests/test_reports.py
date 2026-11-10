import unittest

from features import reports


class TestReports(unittest.TestCase):
    def test_average_score_calculates_history_average(self):
        self.assertEqual(reports.average_score({"history": [5, 6, 4]}), 5.0)

    def test_average_score_returns_zero_for_empty_history(self):
        self.assertEqual(reports.average_score({"history": []}), 0.0)


if __name__ == "__main__":
    unittest.main()
