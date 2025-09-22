# Week 7 - Activity 4: Singeleton and Factory design pattern (due date 25 Sep 2025 )
# Develop a code to show the usage of both design patterns in your coding for; 
# Design a payment processing system that supports multiple payment methods (e.g., Creditcard, PayPal, Bank Transfer, CryptoPayment, GooglePay).
# Use the Factory Design Pattern to create different payment method objects dynamically.
# Ensure the payment gateway (the main entry point for processing payments) is implemented as a Singleton, so only one instance of the gateway exists in the system.


# The abc module provides the infrastructure for defining Abstract Base Classes (ABCs) in Python.
from abc import ABC, abstractmethod

# Singleton Metaclass
# This metaclass ensures that a class has only one instance and provides a global point of access to it.
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
# Payment Gateway Singleton
# The main entry point for processing payments
# This singleton class ensures only one instance of the payment gateway exists
class PaymentGateway(metaclass=SingletonMeta):
    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)
        print(f"Processed payment of ${amount} using {payment_method.__class__.__name__}\n")

# Abstract Payment Method
# This abstract class defines the interface for different payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Payment Methods
# These classes are implementations of different payment methods
# If new payment methods are to be added, new classes can be created here
class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with Credit Card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with Bank Transfer")

class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with Cryptocurrency")

class GooglePay(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with Google Pay")

# New and additional payment method example
class EFTPOS(PaymentMethod):
    def pay(self, amount):
        print(f"Paying ${amount} with EFTPOS")

# Factory for creating payment methods
# This factory class is responsible for creating instances of different payment methods based on the input type
# When new payment methods are added, the factory method can be updated to include them
# You just need to add a new class and update the factory method
class PaymentMethodFactory:
    @staticmethod
    def create_payment_method(method_type):
        if method_type == "creditcard":
            return CreditCard()
        elif method_type == "paypal":
            return PayPal()
        elif method_type == "banktransfer":
            return BankTransfer()
        elif method_type == "cryptopayment":
            return CryptoPayment()
        elif method_type == "googlepay":
            return GooglePay()
        elif method_type == "eftpos":
            return EFTPOS()
        else:
            raise ValueError(f"Unknown payment method: {method_type}")


if __name__ == "__main__":
    
    # Singleton Payment Gateway instance calls the process_payment method
    # This makes sure that only one instance of PaymentGateway is used throughout the application
    gateway = PaymentGateway()

    # Factory-created payment methods
    # This loop creates different payment method instances using the factory and processes payments
    # New payment methods can be added by simply updating the PaymentMethodFactory without changing the client code
    payment_methods = ["creditcard", "paypal", "banktransfer", "cryptopayment", "googlepay", "eftpos"]
    amounts = [100, 200, 300, 400, 500, 20]

    # This loop processes payments using different payment methods created by the factory
    for method, amount in zip(payment_methods, amounts):
        payment_method = PaymentMethodFactory.create_payment_method(method)
        gateway.process_payment(payment_method, amount)




