"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_check_answer_is_case_insensitive(self):
        card = {"id": 1, "question": "Capital of France?", "answer": "Paris", "category": "geo"}
        self.assertTrue(core.check_answer(card, "paris"))
        self.assertFalse(core.check_answer(card, "London"))

    def test_add_card_gives_a_new_id(self):
        data = {"cards": [{"id": 1, "question": "q", "answer": "a", "category": "general"}]}
        card = core.add_card(data, "New question?", "yes")
        self.assertEqual(card["id"], 2)
        self.assertEqual(len(data["cards"]), 2)

    def test_progress_bar_formats_positions_and_boundaries(self):
        self.assertEqual(core.progress_bar(3, 8), "[###-------] 3/8")
        self.assertEqual(core.progress_bar(0, 8), "[----------] 0/8")
        self.assertEqual(core.progress_bar(8, 8), "[##########] 8/8")

    def test_run_quiz_shows_progress_before_each_question(self):
        cards = [
            {"question": "First?", "answer": "yes"},
            {"question": "Second?", "answer": "no"},
        ]
        shown = []

        core.run_quiz(cards, ask=lambda _: "", show=shown.append)

        self.assertEqual(shown[0], "[#####-----] 1/2")
        self.assertEqual(shown[2], "[##########] 2/2")


if __name__ == "__main__":
    unittest.main()
