# Week 7 Activity 2 - Factory Design Pattern. 

# Initial code - tightly coupled and repetitive
# Payment processing system with multiple payment methods
# Each payment method has its own class and the client code directly instantiates them.
# This leads to code duplication and difficulty in adding new payment methods.


# Payment processor classes
class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class ApplePayPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Apple Pay"
    
# Factory Design Pattern Implementation
# This factory class is responsible for creating payment processor instances
# instead of the client code directly instantiating them
class PaymentFactory:
    _processors = {
        "paypal": PayPalPayment, 
        "stripe": StripePayment,
        "credit_card": CreditCardPayment,
        "apple_pay": ApplePayPayment
    }
    
    # Static method to get the appropriate payment processor
    # This method abstracts the instantiation logic from the client code
    # making it easier to add new payment methods in the future
    @staticmethod
    def get_payment_processor(pay_method):
        processor_class = PaymentFactory._processors.get(pay_method.lower())
        if not processor_class:
            raise ValueError(f"Unknown payment method: {pay_method}")
        return processor_class()

# Client code using the factory to get payment processors
def checkout(pay_method, amount):
    processor = PaymentFactory.get_payment_processor(pay_method)
    return processor.process_payment(amount)

#Test the refactored code
print(checkout("paypal", 100))
print(checkout("stripe", 150))
print(checkout("credit_card", 200))
print(checkout("apple_pay", 250)) 

