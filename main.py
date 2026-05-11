# 2-misol
class Car:
    wheels = 4
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def car_info(self):
        print(f"brand: {self.brand}")
        print(f"color: {self.color}")
        print(f"year: {self.year}")
        print(f"wheels: {Car.wheels}")

c1 = Car("BMW", "black", "2020")
c1.car_info()

print()

c2 = Car("Mers", "white", "2015")
c1.car_info()

# 3-misol
class Phone:
    country = "China"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_phone(self):
        print(f"brand: {self.brand}")
        print(f"price: {self.price}")
        print(f"country: {Phone.country}")

p1 = Phone("Iphone", 100000)
p1.show_phone()

p2 = Phone("Samsung", 8000)
p2.show_phone()

# 4-misol
class Employee:
    company_name = "Google"

    def __init__(self, fullname, salary, position):
        self.fullname = fullname
        self.salary = salary
        self.position = position

    def employee_info(self):
        print(f"fullname: {self.fullname}")
        print(f"salary: {self.salary}")
        print(f"position: {self.position}")
        print(f"company_name: {self.company_name}")

e1 = Employee("Ali", 12000, "funny")
e1.employee_info()
print(Employee.employee_info())
