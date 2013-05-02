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
        result = ironman.apriori.get_frequency(self.transaction)
        self.assertEqual(result, {"{'a'}": 3, "{'b'}": 6, "{'c'}": 4, "{'d'}": 5}, "Get frequency test")

    @unittest.skip
    def test_get_next_length_set(self):
        s = [{'a'}, {'b'}, {'c'}, {'d'}]
        expected  = [{'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'c'}, {'b', 'd'}, {'c', 'd'}]
        for x in ironman.functions.get_next_length_set(s):
            self.assertTrue(x in expected, "Get next length set => {0}".format(x))

    def test_get_association_rules(self):
        result = ironman.apriori.get_association_rules(self.transaction)
        self.assertEqual(result[0], {'b', 'c', 'd'}, "Apriori test")
