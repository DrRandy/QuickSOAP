import unittest
import quick
from quick import convert


class TestTextbox(unittest.TestCase):

    def test_TextboxAnonymous(self):
        input = "`@"
        output = "[text]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxAnonymous did not parse correctly")

    def test_TextboxAnonymousDefaultText(self):
        input = "`@=\"default text\""
        output = "[text value=\"default text\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxAnonymousDefaultText did not parse correctly")

    def test_TextboxNamed(self):
        input = "`@fieldname"
        output = "[text name=\"fieldname\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxNamed did not parse correctly")

    def test_TextboxNamedDefaultText(self):
        input = "`@fieldname=\"default text\""
        output = "[text name=\"fieldname\" value=\"default text\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxNamedDefaultText did not parse correctly")

    def test_TextboxAnonymousPlusBoilerplate(self):
        input = "Please enter your name: `@"
        output = "Please enter your name: [text]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxAnonymousPlusBoilerplate did not parse correctly")

    def test_TextboxAnonymousDefaultTextPlusBoilerplate(self):
        input =  "Today is a `@=\"wonderful\" day!"
        output = "Today is a [text value=\"wonderful\"] day!"
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxAnonymousDefaultTextPlusBoilerplate did not parse correctly")

    def test_TextboxNamedPlusBoilerplate(self):
        input = "Your favorite color is `@color."
        output = "Your favorite color is [text name=\"color\"]."
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxNamedPlusBoilerplate did not parse correctly")

    def test_TextboxNamedDefaultTextPlusBoilerplate(self):
        input = "Your favorite color is `@color=\"blue\"."
        output = "Your favorite color is [text name=\"color\" value=\"blue\"]."
        test_output = convert(input)
        self.assertEqual(output, test_output, "TextboxNamedDefaultTextPlusBoilerplate did not parse correctly")

class TestDropdown(unittest.TestCase):

    def test_DropdownAnonymous(self):
        input = "`^=\"option 1|option 2\""
        output = "[select value=\"option 1|option 2\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "DropdownAnonymous did not parse correctly")

    def test_DropdownNamed(self):
        input = "`^fieldname=\"option 1|option 2\""
        output = "[select name=\"fieldname\" value=\"option 1|option 2\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "DropdownNamed did not parse correctly")

class TestCheckbox(unittest.TestCase):

    def test_CheckboxAnonymous(self):
        input = "`+"
        output = "[checkbox]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "CheckboxAnonymous did not parse correctly")

    def test_CheckboxAnonymousCaption(self):
        input = "`+=\"caption for checkbox\""
        output = "[checkbox value=\"caption for checkbox\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "CheckboxAnonymousCaption did not parse correctly")

    def test_CheckboxNamed(self):
        input = "`+fieldname"
        output = "[checkbox name=\"fieldname\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "CheckboxNamed did not parse correctly")

    def test_CheckboxNamedCaption(self):
        input = "`+fieldname=\"caption for checkbox\""
        output = "[checkbox name=\"fieldname\" value=\"caption for checkbox\"]"
        test_output = convert(input)
        self.assertEqual(output, test_output, "CheckboxNamedCaption did not parse correctly")


if __name__=="__main__":
    unittest.main()

