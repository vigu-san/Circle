class ShoppingCart():
    def __init__(self):
        self.items = []

    def addToCart(self, itemname, quantity):
        item = (itemname, quantity)
        self.items.append(item)

    def removeFromCart(self, itemname):
        for item in self.items:
            if item[0] == itemname:
                self.items.remove(item)
                break

    def total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

