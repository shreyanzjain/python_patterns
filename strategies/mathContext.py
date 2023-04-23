from mathStrategy import IMathStrategy


class Context:
    def __init__(self):
        self.strat = IMathStrategy

    def setStrategy(self, strategy):
        self.strat = strategy

    def executeStrategy(self, a, b):
        return self.strat.operation_method(a, b)
