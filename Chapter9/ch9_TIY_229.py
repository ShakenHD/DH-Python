class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'{self.restaurant_name}\n{self.cuisine_type}')

    def open_restaurant(self):
        print('The restaurant is now open.')

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, num_served):
        self.number_served += num_served

my_restaurant = Restaurant("Dan's Diner", "Health Food", 12)
Restaurant.set_number_served(my_restaurant, 25)
Restaurant.increment_number_served(my_restaurant, 5)

print(f'Restaurant: \t{my_restaurant.restaurant_name}\nCuisine Type:\t{my_restaurant.cuisine_type}\nNumber Served:\t{my_restaurant.number_served}')

Restaurant.describe_restaurant(my_restaurant)
Restaurant.open_restaurant(my_restaurant)

print('\n')


class User:
    def __init__(self, f_name, l_name, gender, log_attempts):
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.log_attempts = log_attempts

    def describe_user(self):
        print(f'First name:\t{self.f_name}\nLast Name:\t{self.l_name}\nGender:\t\t{self.gender}\nLogin Attempts:\t{self.log_attempts}')

    def greet_user(self):
        print(f'Sup {self.f_name} {self.l_name}. How are you doing?')

    def increment_attempts_by_1(self):
        self.log_attempts += 1
    def reset_attempts(self):
        self.log_attempts = 0;

my_user = User("Daniel", 'Hockley', 'Male', 22)
User.greet_user(my_user)

User.increment_attempts_by_1(my_user)
User.describe_user(my_user)
print('\n')

User.reset_attempts(my_user)
User.describe_user(my_user)
print('\n')


class Flavours:
    def __init__(self, flavours=["Vanilla", "Choc", "Strawberry"]):
        self.flavours = flavours

    def display_flavours(self):
        print(self.flavours)


class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavor, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = Flavours(flavor)


my_stand = IcecreamStand('Dans CREAMING', 'Dessert', ['ss','aa','oo'], 22)

my_stand.flavours.display_flavours()



class Priviledges:
    def __init__(self, priviledge):
        self.priviledge = priviledge


class Admin(User):
    def __init__(self, f_name, l_name, gender, log_attempts, priv):
        super().__init__(f_name, l_name, gender, log_attempts)
        self.priv = priv



