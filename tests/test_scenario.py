import unittest
import objectbdd

class TestPyBddScenario(unittest.TestCase):
  def setUp(self):
    self.methods_called = []

  def test_thing(self):
    objectbdd.Scenario(self).describe("""
      Given given is called
      When when is called
      Then then is called
      And and is called
      Then pybdd scenario is implemented
    """)

  def given_is_called(self):
    self.methods_called.append("given_is_called")

  def when_is_called(self):
    self.methods_called.append("when_is_called")

  def then_is_called(self):
    self.methods_called.append("then_is_called")

  def and_is_called(self):
    self.methods_called.append("and_is_called")

  def some_other_method(self):
    pass

  def pybdd_scenario_is_implemented(self):
    self.assertEqual(self.methods_called, ['given_is_called', 'when_is_called', 'then_is_called', 'and_is_called'])


