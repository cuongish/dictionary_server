import unittest
import app


class BaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.setUp()

    def tearDown(self) -> None:
        self.tearDown()

    def test_home__html_does_not_crash(self):
        pass

    def test_save__returns_200_if_posts_correct_schema_format(self):
        pass

    def test_save__returns_400_if_posts_wrong_schema_format(self):
        pass

    def test_save__updates_table_if_posts_duplicated_key(self):
        pass

    def test_load__gets_correct_value_if_key_was_saved(self):
        pass

    def test_load__returns_404_if_key_was_not_saved(self):
        pass


if __name__ == '__main__':
    unittest.main()