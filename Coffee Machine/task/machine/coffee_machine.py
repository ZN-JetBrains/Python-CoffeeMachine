class CoffeeMachine:
    n_machines = 0

    def __new__(cls, *args, **kwargs):
        if cls.n_machines == 0:
            cls.n_machines += 1
            return object.__new__(cls)
        return None

    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups

    def __repr__(self):
        return f"CoffeeMachine({self.money}, {self.water}, {self.milk}, {self.beans}, {self.cups})"

    def __str__(self):
        return f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        ${self.money} of money"""

    def can_buy_espresso(self):
        if not self.water >= 250:
            print("Sorry, not enough water!")
            return False
        if not self.beans >= 16:
            print("Sorry, not enough beans!")
            return False
        if not self.cups >= 1:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def can_buy_latte(self):
        if not self.water >= 350:
            print("Sorry, not enough water!")
            return False
        if not self.milk >= 75:
            print("Sorry, not enough milk!")
            return False
        if not self.beans >= 20:
            print("Sorry, not enough beans!")
            return False
        if not self.cups >= 1:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def can_buy_cappuccino(self):
        if not self.water >= 200:
            print("Sorry, not enough water!")
            return False
        if not self.milk >= 100:
            print("Sorry, not enough milk!")
            return False
        if not self.beans >= 12:
            print("Sorry, not enough beans!")
            return False
        if not self.cups >= 1:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self, a_beverage):
        if a_beverage == 1 and self.can_buy_espresso():
            self.money += 4
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
        elif a_beverage == 2 and self.can_buy_latte():
            self.money += 7
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
        elif a_beverage == 3 and self.can_buy_cappuccino():
            self.money += 6
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1

    def fill(self):
        print("Write how many ml of water do you want to add:")
        fill_water = int(input())
        self.water += fill_water
        print("Write how many ml of milk do you want to add:")
        fill_milk = int(input())
        self.milk += fill_milk
        print("Write how many grams of coffee beans do you want to add:")
        fill_beans = int(input())
        self.beans += fill_beans
        print("Write how many disposable cups of coffee do you want to add:")
        fill_cups = int(input())
        self.cups += fill_cups

    def interact(self, action):
        if action == "buy":
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            choice = input()
            if not choice == "back":
                beverage = int(choice)
                self.buy(beverage)
            print()
        elif action == "fill":
            print()
            self.fill()
            print()
        elif action == "take":
            print(f"\nI gave you ${coffee_machine.money}\n")
            self.money -= coffee_machine.money
        elif action == "remaining":
            print()
            print(self)
            print()
        elif action == "exit":
            return False
        return True


# Instantiate coffee machine
coffee_machine = CoffeeMachine(550, 400, 540, 120, 9)

# Application Loop
is_running = True
while is_running:
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = input()
    is_running = coffee_machine.interact(user_action)
