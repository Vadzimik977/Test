import unittest

class TestGetScore(unittest.TestCase):
    def setUp(self):
        # Define a sample game stamps data for testing
        self.game_stamps = [
            {"offset": 0, "score": {"home": 0, "away": 0}},
            {"offset": 10, "score": {"home": 1, "away": 0}},
            {"offset": 20, "score": {"home": 1, "away": 1}},
            {"offset": 30, "score": {"home": 2, "away": 1}},
        ]

    def test_score_at_offset(self):
        # Test for a specific offset where a score is expected
        home_score, away_score = get_score(self.game_stamps, 15)
        self.assertEqual(home_score, 1)
        self.assertEqual(away_score, 0)

    def test_score_before_first_offset(self):
        # Test for an offset before the first stamp's offset
        home_score, away_score = get_score(self.game_stamps, -5)
        self.assertIsNone(home_score)
        self.assertIsNone(away_score)

    def test_score_after_last_offset(self):
        # Test for an offset after the last stamp's offset
        home_score, away_score = get_score(self.game_stamps, 35)
        self.assertEqual(home_score, 2)
        self.assertEqual(away_score, 1)

    def test_exact_offset(self):
        # Test for an offset exactly matching a stamp's offset
        home_score, away_score = get_score(self.game_stamps, 20)
        self.assertEqual(home_score, 1)
        self.assertEqual(away_score, 1)

if __name__ == '__main__':
    unittest.main()
