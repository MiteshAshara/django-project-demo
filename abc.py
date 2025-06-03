# x=10
# def name(name,age): #Postional argument (exact postion known for run ,Order matters)
#     global x #10
#     print(f"Name: {name}, Age: {age}")
#     print("Before : ",x) 
#     x=20
#     print("After : " ,x)
# print(x)
# name("John", 30)  
# print(x)


# class Vehicle:
#     def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
#         self.number_of_wheels = number_of_wheels
#         self.type_of_tank = type_of_tank
#         self.seating_capacity = seating_capacity
#         self.maximum_velocity = maximum_velocity

#     def make_noise(self):
#         print('VRUUUUUUUM')
        
#     def run(self):
#         print(f"The vehicle is running with {self.maximum_velocity} km/h maximum velocity")

# # Create a vehicle instance
# car = Vehicle(4, 'gasoline', 5, 180)

# # Call methods
# car.make_noise()
# car.run()
# def hello(name):
#     print('Hello ' + name + '!')

# hello("Alice")  

# def hello(name):
#     print('Hello ' + name + '!')

# user_name = input("Enter your name: ")
# hello(user_name)

# def hello(name, age):
#     print('Hello ' + name + ', you are ' + str(age) + ' years old!')

# hello("Alice", 30)

# val = 1

# def change():
#     global val
#     val = 2

# change()
# print(val)

# def hello(name):
#     print('Hello ' + name + '!')
#     return name

# returned_name = hello("Alice")

# print("Returned value:", returned_name)

# def factorial(n):
#     if n == 1: 
#         return 1
#     return n * factorial(n - 1)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(3))  # 6
# print(factorial(4))  # 24
# print(factorial(5))  # 120

