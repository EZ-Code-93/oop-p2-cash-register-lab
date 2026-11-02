#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.previous_transactions = []

  @property
  def total(self):
    return self._total

  @total.setter
  def total(self, value):
    if not isinstance(value, (int, float)) or value < 0:
      raise ValueError("Total must be a non-negative number")
    self._total = round(value, 2)

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if type(value) is not int or value < 0 or value > 100:
      raise ValueError("Discount must be a non-negative integer between 0 and 100")
    self._discount = value

  def add_item(self, item, price, quantity=1):
    if not isinstance(price, (int, float)) or price < 0:
      raise ValueError("Price must be a non-negative number")
    if type(quantity) is not int or quantity < 1:
      raise ValueError("Quantity must be a positive integer")
    self.items.extend([item] * quantity)
    self.previous_transactions.append((price * quantity, quantity))
    self.total += price * quantity
    return self.total

  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total - (self.total * self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total) if self.total.is_integer() else self.total}.")
    else:
      print("There is no discount to apply.")
    return self.total
  
  def void_last_transaction(self):
    if self.previous_transactions:
      last_price, last_quantity = self.previous_transactions.pop()
      self.total -= last_price
      for _ in range(last_quantity):
        self.items.pop()