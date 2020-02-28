'''
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
'''


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        combination = []
        for i in range(len(self.ingredients)):
            for k in range(len(self.toppings)):
                combination.append([self.ingredients[i], self.toppings[k]])
        return combination


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
machine2 = IceCreamMachine(["vanilla"], ["chocolate sauce","cheese sauce"])
machine3 = IceCreamMachine([], [])
machine4 = IceCreamMachine(["vanilla", "chocolate","cheese"], ["chocolate sauce","cheese sauce"])
print(machine.scoops())
print(machine2.scoops())
print(machine3.scoops())
print(machine4.scoops())
