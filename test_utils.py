import unittest

from utils import calculate_average, get_user_name


class TestCalculateAverage(unittest.TestCase):
    def test_list_of_integers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4]), 2.5)

    def test_floats(self):
        self.assertAlmostEqual(calculate_average([0.1, 0.2, 0.3]), 0.2)

    def test_single_value(self):
        self.assertEqual(calculate_average([7]), 7)

    def test_negative_values(self):
        self.assertEqual(calculate_average([-2, -4, 6]), 0)

    def test_accepts_generator(self):
        self.assertEqual(calculate_average(x for x in range(5)), 2)

    def test_accepts_tuple(self):
        self.assertEqual(calculate_average((10, 20)), 15)

    def test_empty_list_raises(self):
        with self.assertRaisesRegex(ValueError, "empty"):
            calculate_average([])

    def test_empty_generator_raises(self):
        with self.assertRaises(ValueError):
            calculate_average(x for x in [])

    def test_none_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "None"):
            calculate_average(None)

    def test_non_numeric_element_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "numeric"):
            calculate_average([1, "2", 3])

    def test_none_element_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "numeric"):
            calculate_average([1, None])

    def test_string_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            calculate_average("123")

    def test_bool_element_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "numeric"):
            calculate_average([True, False])


class TestGetUserName(unittest.TestCase):
    def test_returns_upper_case_name(self):
        self.assertEqual(get_user_name({"name": "alice"}), "ALICE")

    def test_preserves_other_fields_untouched(self):
        user = {"name": "Bob", "age": 30}
        self.assertEqual(get_user_name(user), "BOB")
        self.assertEqual(user, {"name": "Bob", "age": 30})

    def test_unicode_name(self):
        self.assertEqual(get_user_name({"name": "zoë"}), "ZOË")

    def test_missing_name_raises(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            get_user_name({"age": 30})

    def test_empty_dict_raises(self):
        with self.assertRaises(ValueError):
            get_user_name({})

    def test_empty_name_raises(self):
        with self.assertRaisesRegex(ValueError, "non-empty string"):
            get_user_name({"name": ""})

    def test_whitespace_name_raises(self):
        with self.assertRaisesRegex(ValueError, "non-empty string"):
            get_user_name({"name": "   "})

    def test_none_name_raises(self):
        with self.assertRaisesRegex(ValueError, "non-empty string"):
            get_user_name({"name": None})

    def test_non_string_name_raises(self):
        with self.assertRaisesRegex(ValueError, "non-empty string"):
            get_user_name({"name": 42})

    def test_none_user_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "None"):
            get_user_name(None)

    def test_non_mapping_user_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "mapping"):
            get_user_name(["name"])


if __name__ == "__main__":
    unittest.main()
