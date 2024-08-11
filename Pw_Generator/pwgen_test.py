import unittest
import pwgen

def assert_exact_character_category_count_in_pw(self, exp_alpha, exp_num, exp_special):
    password = pwgen.pwgen(exp_alpha, exp_num, exp_special)
    print("---" + password + "---")

    alpha_count = 0
    num_count = 0
    special_count = 0
    for i in range(len(password)):
        if password[i].isalpha():
            alpha_count += 1
        elif password[i].isnumeric():
            num_count += 1
        else:
            special_count += 1

    self.assertEqual(exp_num, num_count)
    self.assertEqual(exp_alpha, alpha_count)
    self.assertEqual(exp_special, special_count)


class PwgenTest(unittest.TestCase):
    def test_password_has_the_given_number_of_symbols(self):
        assert_exact_character_category_count_in_pw(self, 3, 5, 2)

    def test_password_missing_letters_category(self):
        assert_exact_character_category_count_in_pw(self, 0, 3, 7)
        assert_exact_character_category_count_in_pw(self, 2, 0, 5)
        assert_exact_character_category_count_in_pw(self, 4, 3, 0)
        assert_exact_character_category_count_in_pw(self, 0, 0, 0)

if __name__ == '__main__':
    unittest.main()
