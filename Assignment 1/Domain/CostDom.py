class CostDom:
    def __init__(self, cost):
        self._cost = cost

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = new_cost

