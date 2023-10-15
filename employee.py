"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        pass

class EmployeeHourly(Employee):
    def __init__(self, name, hourlyRate, hours):
        super().__init__(name)
        self.hourlyRate = hourlyRate
        self.hours = hours

    def get_pay(self):
        return self.hourlyRate * self.hours
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hourlyRate}/hour. Their total pay is {self.get_pay()}'
    
class EmployeeMonthly(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.monthlySalary = salary

    def get_pay(self):
        return self.monthlySalary
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.monthlySalary}. Their total pay is {self.get_pay()}'

class EmployeeMonthlyWithContractCommission(EmployeeMonthly):
    def __init__(self, name, salary, commissionRate, commissions):
        super().__init__(name, salary)
        self.commissionRate = commissionRate
        self.commissionContracts = commissions
    
    def get_pay(self):
        return super().get_pay() + (self.commissionContracts * self.commissionRate)
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.monthlySalary} and receives a commission for {self.commissionContracts} contract(s) at {self.commissionRate}/contract. Their total pay is {self.get_pay()}'

class EmployeeMonthlyWithBonusCommission(EmployeeMonthly):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonusCommission = bonus

    def get_pay(self):
        return super().get_pay() + self.bonusCommission
    
    def __str__(self):
        return f'{self.name} works on a monthly salary of {self.monthlySalary} and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}'

class EmployeeHourlyWithContractCommission(EmployeeHourly):
    def __init__(self, name, hourlyRate, hours, commissionRate, commissions):
        super().__init__(name, hourlyRate, hours)
        self.commissionRate = commissionRate
        self.commissionContracts = commissions

    def get_pay(self):
        return super().get_pay() + (self.commissionContracts * self.commissionRate)
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} hours at {self.hourlyRate}/hour and receives a commission for {self.commissionContracts} contract(s) at {self.commissionRate}/contract. Their total pay is {self.get_pay()}'

class EmployeeHourlyWithBonusCommission(EmployeeHourly):
    def __init__(self, name, hourlyRate, hours, bonus):
        super().__init__(name, hourlyRate, hours)
        self.bonusCommission = bonus

    def get_pay(self):
        return super().get_pay() + self.bonusCommission
    
    def __str__(self):
        return f'{self.name} works on a contract of {self.hours} at {self.hourlyRate}/hour and receives a bonus commission of {self.bonusCommission}. Their total pay is {self.get_pay()}'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = EmployeeMonthly('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = EmployeeHourly('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = EmployeeMonthlyWithContractCommission('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = EmployeeHourlyWithContractCommission('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = EmployeeMonthlyWithBonusCommission('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = EmployeeHourlyWithBonusCommission('Ariel', 30, 120, 600)