import unittest
import sys

sys.path.insert(0, 'C:/Users/sumkukre/Desktop/programing/FlaskDev/xzceb-flask_eng_fr/final_project/machinetranslation')

from machinetranslation import translator
class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(translator.englishToFrench('Hello') , 'Bonjour')
    

    def test_french_to_english(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')
if __name__ == '__main__':
    unittest.main()