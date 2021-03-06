# Object BDD for Python

Object BDD is a lightweight testing tool for describing the 
behaviors of your software that the stakeholders expect to 
be able to observe.

Object BDD is intended to be used while writing xUnit-style tests 
and aims to keep the scenario steps close to the implementation.
Other Python-based BDD tools separate stories from implentation: 
see Behave or Lettuce.


## Install


    pip install objectbdd


## Usage


    import unittest
    import objectbdd

    class TestCustomerPayment(unittest.TestCase):
        def setUp(self):
            self.scenario = objectbdd.Scenario(self)
            self.scenario.describe("""
                Given I am a customer on the checkout page
            """)

        def test_customer_can_pay(self):
            self.scenario.describe("""
                When I enter my credit card details
                Then I should receive a payment confirmation
            """)

        def test_customer_can_pay(self):
            self.scenario.describe("""
                When I enter my invalid credit card details
                Then I should receive a warning
            """)

        def i_am_a_customer_on_the_checkout_page(self):
            # ... write some logic

        def i_enter_my_credit_card_details(self):
            # ... interact with your system

        def i_should_receive_a_payment_confirmation(self):
            # ... assert the expected behavior

        # ... additional methods


## Improving objectbdd / Development Environment


    mkvirtualenv objectbdd-test
    ./scripts/build.sh


Please create issues on Github if you have bugs or feature requests.  Pull-requests are welcome.


## Thanks

Inspiration for objectbdd comes from Ruby's Simple BDD library:  https://github.com/robb1e/simple_bdd
