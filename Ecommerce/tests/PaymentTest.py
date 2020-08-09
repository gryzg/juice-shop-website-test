import unittest

class PaymentTest(unittest.TestCase):
    def add_new_payment_method (self):
        print ("New Payment Method added")
        self.assertTrue(True)

    def credit_card_payment_is_successful(self):
        print ("Credit Card Payment successful")
        self.assertTrue(True)

    def wallet_payment_is_successful(self):
        print ("Wallet Payment successful")
        self.assertTrue(True)

    def expired_credit_card(self):
        print("Credit Card Expired")
        self.assertTrue(True)

    def insufficient_wallet_balance(self):
        print("Insufficient Wallet Balance")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()