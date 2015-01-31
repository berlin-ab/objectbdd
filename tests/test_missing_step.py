import unittest
import objectbdd.exceptions

class TestMissingStep(unittest.TestCase):

  def setUp(self):
      self.scenario = objectbdd.Scenario(self)
      self.exception = None

      try:
          self.scenario.describe("""
              Given I have defined methods for only a portion of my tests 
              When I leave a step undefined
          """)
      except objectbdd.exceptions.StepNotDefined as error:
          self.exception = error

      self.scenario.describe("""
          Then I should see an exception from objectbdd
      """)

  def i_have_defined_methods_for_only_a_portion_of_my_tests(self):
      pass

  def i_should_see_an_exception_from_objectbdd(self):
      self.assertIsNotNone(self.exception)
      self.assertEquals(self.exception.message, """
          Missing:

          def i_leave_a_step_undefined(self):
              pass

      """)


