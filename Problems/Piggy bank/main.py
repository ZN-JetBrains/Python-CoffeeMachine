class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            dollars_to_add = self.cents // 100
            remaining_cents = self.cents - (dollars_to_add * 100)
            self.dollars += dollars_to_add
            self.cents = remaining_cents
