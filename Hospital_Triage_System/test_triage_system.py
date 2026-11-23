import unittest
from triage_system import Triage_System

class TestTriageSystem(unittest.TestCase):

    def test_higher_severity_first(self):
        test = Triage_System()
        test.add_patient("Sally", 1)
        test.add_patient("Mike", 4)
        test.add_patient("Tracy", 3)
        test.add_patient("Tim", 5)
        test.add_patient("Paulo", 2)
        self.assertEqual(test.process_next(), ('Tim', 5))
        self.assertEqual(test.process_next(), ('Mike', 4))
        self.assertEqual(test.process_next(), ('Tracy', 3))
        self.assertEqual(test.process_next(), ('Paulo', 2))
        self.assertEqual(test.process_next(), ('Sally', 1))

    def test_arrival_order(self):
        test = Triage_System()
        test.add_patient("Sally", 3)
        test.add_patient("Mike", 3)
        test.add_patient("Tracy", 3)
        test.add_patient("Tim", 3)
        test.add_patient("Paulo", 3)
        self.assertEqual(test.process_next(), ('Sally', 3))
        self.assertEqual(test.process_next(), ('Mike', 3))
        self.assertEqual(test.process_next(), ('Tracy', 3))
        self.assertEqual(test.process_next(), ('Tim', 3))
        self.assertEqual(test.process_next(), ('Paulo', 3))

    def test_peek_next_functionality(self):
        test = Triage_System()
        test.add_patient("Sally", 3)
        test.add_patient("Mike", 3)
        test.add_patient("Tracy", 3)
        test.add_patient("Tim", 3)
        test.add_patient("Paulo", 3)
        self.assertEqual(test.size(), 5)





