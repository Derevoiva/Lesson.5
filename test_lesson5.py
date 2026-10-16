import unittest
import lesson5 as m

class LessonTests(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(m.subject_hours(["Physics: 30(л) — 10(лаб)"]),{"Physics":40})
        self.assertEqual(m.translate_numerals("One — 1"),"Один — 1")
        self.assertEqual(m.company_profits(["Firm Ltd 10 6","Loss Inc 2 4"])[1]["average_profit"],4)

if __name__ == "__main__":
    unittest.main()
