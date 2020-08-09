import unittest
from tests.LoginTest import LoginTest
from tests.OrderPlacementTest import OrderPlacementTest
from tests.PaymentTest import PaymentTest

#Get all test methods
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
order_test = unittest.TestLoader().loadTestsFromTestCase(OrderPlacementTest)
payment_test = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

sanity_test = unittest.TestSuite([login_test])
functional_test = unittest.TestSuite ([login_test, order_test, payment_test])
unittest.TextTestRunner(verbosity=2).run(functional_test)
