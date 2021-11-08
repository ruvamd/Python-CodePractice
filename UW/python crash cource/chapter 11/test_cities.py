import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    def test_city_country(self):
        formtd_city_country_population=city_country('seattle','usa','3000000')
        self.assertEqual(formtd_city_country_population,'Seattle Usa 3000000')
if __name__=='__main__':
    unittest.main()
