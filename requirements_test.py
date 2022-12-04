import unittest
from requirements import *

req_cases = [
    "Profesja: Gladiator, Budowa 16+, Bijatyka lub Sztuki walki lub Broń ręczna 7+",
    "Spryt 10+, Postrzeganie emocji lub Blef 2+",
    "Bumerang 4+, Zręczność 12+",
    "Percepcja 15+, Postrzeganie emocji 4+",
    "Umiejętność z grupy Prowadzenie Pojazdów 3+, Charakter 8+",
    "dowolna umiejętność z grupy Prowadzenie pojazdów 5+, Mechanika 5+, Fizyka 2+",
    "Zastraszanie 5+, Zdolności przywódcze 4+, Charakter 14+"
    "Tylko dla profesji Żołnierz, Morale 4+",
    "Pistolety 3+ lub Karabiny 3+, Charakter 12+, Zręczność 12+"
]

class TestStringMethods(unittest.TestCase):

    def test_wsp(self):
        case = "Zręczność 12+"
        rqs = parseRequirements(case)
        self.assertEqual(len(rqs), 1)
        self.assertEqual(rqs[0].type, REQUIREMENT_TYPE.WSPOLCZYNNIK)
        self.assertEqual(rqs[0].subType, WSPOLCZYNNIK.ZRECZNOSC)
        self.assertEqual(rqs[0].value, 12)

    def test_umiej(self):
        case = "Pistolety 3+"
        rqs = parseRequirements(case)
        self.assertEqual(len(rqs), 1)
        self.assertEqual(rqs[0].type, REQUIREMENT_TYPE.UMIEJETNOSC)
        self.assertEqual(rqs[0].subType, UMIEJETNOSC.PISTOLETY)
        self.assertEqual(rqs[0].value, 3)

    def test_multiple(self):
        case = "Pistolety 3+ lub Karabiny 3+, Charakter 12+, Zręczność 12+"
        rqs = parseRequirements(case)
        self.assertEqual(len(rqs), 3)
        self.assertEqual(rqs[0].type, REQUIREMENT_TYPE.SELECT)
        self.assertEqual(len(rqs[0].children), 2)

        self.assertEqual(rqs[0].children[0].type, REQUIREMENT_TYPE.UMIEJETNOSC);
        self.assertEqual(rqs[0].children[0].subType, UMIEJETNOSC.PISTOLETY);
        self.assertEqual(rqs[0].children[0].value, 3);

        self.assertEqual(rqs[0].children[1].type, REQUIREMENT_TYPE.UMIEJETNOSC);
        self.assertEqual(rqs[0].children[1].subType, UMIEJETNOSC.KARABINY);
        self.assertEqual(rqs[0].children[1].value, 3)

        self.assertEqual(rqs[1].type, REQUIREMENT_TYPE.WSPOLCZYNNIK)
        self.assertEqual(rqs[1].subType, WSPOLCZYNNIK.CHARAKTER)
        self.assertEqual(rqs[1].value, 12)

        self.assertEqual(rqs[2].type, REQUIREMENT_TYPE.WSPOLCZYNNIK)
        self.assertEqual(rqs[2].subType, WSPOLCZYNNIK.ZRECZNOSC)
        self.assertEqual(rqs[2].value, 12)

    def test_complex(self):
        case = "Profesja: Gladiator, Budowa 16+, Bijatyka 7+ lub Sztuki walki 7+ lub Broń ręczna 7+"
        rqs = parseRequirements(case)
        self.assertEqual(len(rqs), 3)


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)