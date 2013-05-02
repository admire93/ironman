import unittest

import ironman.apriori
import ironman.functions

class IronmanFunctionsTestCase(unittest.TestCase):
    def setUp(self):
       self.transaction = [
          {"a", "b", "c", "d"},
          {"a", "b"},
          {"b", "c", "d"},
          {"b", "c"},
          {"a", "b", "d"},
          {"c", "d"},
          {"b", "d"}
        ] 
        
    def test_get_frequency(self):
        result = ironman.apriori.get_frequency(self.transaction, 2)
        self.assertEqual(result, {"{'a'}": 3, "{'b'}": 6, "{'c'}": 4, "{'d'}": 5}, "Get frequency test")

    def test_get_frequency_for(self):
        frequency = ironman.apriori.get_frequency(self.transaction, 2)
        expected_set = {'a', 'b', 'c', 'd'}
        result_set = ironman.functions.get_set_from_keys(frequency)
        self.assertEqual(result_set, expected_set, "Get sets from dict keys")
        r = ironman.apriori.get_frequency_for(expected_set, self.transaction, 2, 2)
        for k, v in r.items():
            self.assertTrue(v >= 2)
