from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via PayPal.")

class StripePayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid {amount} via Stripe.")



def process_payment(processor: PaymentProcessor, amount: int):
    processor.pay(amount)


payment1 = PayPalPayment()
payment2 = StripePayment()



process_payment(payment1, 1000)
process_payment(payment2, 1500)

