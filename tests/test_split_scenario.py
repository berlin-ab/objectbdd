import unittest
import objectbdd


class TestSplitScenario(unittest.TestCase):
  def setUp(self):
    self.scenario = objectbdd.Scenario(self)
    self.called_methods = []

    self.scenario.describe("""
       Given I start a scenario with some context
    """)

  def test_it_can_be_split(self):
    self.scenario.describe("""
       When I run the test
       Then I should continue running
    """)
    self.assertEqual(self.called_methods, ['start', 'running', 'continue'])

  def test_it_can_be_split_again(self):
    self.scenario.describe("""
       And I can run another scenario
    """)
    self.assertEqual(self.called_methods, ['start', 'another'])

  def i_start_a_scenario_with_some_context(self):
    self.called_methods.append('start')

  def i_run_the_test(self):
    self.called_methods.append('running')

  def i_can_run_another_scenario(self):
    self.called_methods.append('another')

  def i_should_continue_running(self):
    self.called_methods.append('continue')
