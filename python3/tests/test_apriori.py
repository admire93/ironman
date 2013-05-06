import unittest

import ironman.apriori

class IronmanAprioriTestCase(unittest.TestCase):
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
    
    def test_association_rules_for(self):
        result = ironman.apriori.get_association_rules_for({"b", "c"}, self.transaction)
        self.assertEqual(result[0], {'b', 'c', 'd'}, "Get association rules for")
