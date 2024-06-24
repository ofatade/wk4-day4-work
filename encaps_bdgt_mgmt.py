# Task 1: Define Budget Category Class

class BudgetCategory:

    def __init__(self, category_name, allocated_budget = 0):
        self.__category_name = category_name # Private attribute
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

# Task 2: Implement Getters and Setters

    # Getter
    def get_category_name(self):
        return self.__category_name
    
    # Setter
    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name

    
    # Setter
    def set_allocated_budget(self, new_allocated_budget):
        if new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
            self.__remaining_budget = new_allocated_budget 
        else:
            print("Budget must be a positive number")    

    # Getter
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Getter
    def get_remaining_budget(self):
        return self.__remaining_budget


# Task 3: Add Budget Functionality

    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else:
                print("Expense exceeds the remaining budget")
        else:
            print("Expense amount must be a positive number")


# Task 4: Display Budget Details 

    def display_category_summary(self):
         print(f"Your budget for {self.get_category_name()} is {self.get_allocated_budget()} you have {self.get_remaining_budget()} left")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()