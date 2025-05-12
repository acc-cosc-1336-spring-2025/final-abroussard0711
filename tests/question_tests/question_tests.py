#write function tests here, don't add input('') statements here!
import unittest

from src.question_c.question_c import get_most_likely_ancestor_consensus, test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_most_likely_ancestor_consensus (self):
        
        result = get_most_likely_ancestor_consensus ("GATATATGCATATACT", "ATAT")

        pos1, pos2, pos3 = result
        
        self.assertEqual (result, (2, 4, 10))


