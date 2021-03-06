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
        
    def test_get_frequency_for(self):
        result = ironman.apriori.get_frequency_for([], self.transaction, 1)
        self.assertEqual(result, {"{'a'}": 3, "{'b'}": 6, "{'c'}": 4, "{'d'}": 5}, "Get frequency test")
 
    def test_get_association_rules(self):
        result = ironman.apriori.get_association_rules(self.transaction)
        self.assertEqual(result[0], {'b', 'c', 'd'}, "Apriori test")
