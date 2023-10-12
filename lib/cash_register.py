#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0  # To keep track of the last transaction amount

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item_name)
        self.last_transaction = price * quantity  # Update last transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100.0
            self.total -= discount_amount
            return f"Discounted total: ${self.total}"
        else:
            return "No discount to apply"

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            last_price = self.last_transaction
            self.total -= last_price
            return f"Removed last transaction: {last_item} (${last_price})"
        else:
            return "No transactions to void"
