import sys


class Car :
    car_type = "unknown"
    car_types = ('sports_car', 'usual_car', 'not_a_car')
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed



# choosing car type method
    @classmethod
    def choose_type(cls, speed):
        if 120 < int(speed) < 300:
            cls.car_type = cls.car_types[0]
        elif 45 < int(speed) < 120:
            cls.car_type = cls.car_types[1]
        else:
            cls.car_type = cls.car_types[2]



car = Car(input("Choose color: "),input("Choose max speed (in mph): "))

car.color.lower()
car.color = car.color.strip()
car.color = "".join(car.color.split())
car.speed = car.speed.strip()
car.speed = "".join(car.speed.split())


try:
    if car.speed.isdigit():
        car.choose_type(car.speed)
    elif car.speed.isalpha():
        raise ValueError
    elif car.speed.isalnum():
        raise ValueError
    else:
        raise Exception
except ValueError:
    print("Restart script and enter your speed only indigits!")
    sys.exit("Error occured. \n Press F to pay respect. \n Restart script.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    sys.exit("Error occured. \n Press F to pay respect. \n Restart script.")

if car.color.isdigit():
    print('You need to enter your color by letters! Try again.')
    sys.exit("Error occured. \n Press F to pay respect. \n Restart script.")
elif not car.color.isalpha():
    print('You need to enter your color by letters! Try again.')
    sys.exit("Error occured. \n Press F to pay respect. \n Restart script.")


if car.car_type == "sports_car":
    print(f'Your car is {car.color}')
    print("This is fast car!")
    print(f"And it has max speed - {car.speed} mph")
elif car.car_type == "usual_car":
    print(f'Your car is {car.color}')
    print("Good car, mate!")
    print(f"And it has max speed - {car.speed} mph")
elif car.car_type == "not_a_car":
    if int(car.speed) > 300:
        print(f'It is {car.color}, but!')
        print("It's a jet! Not a car!")
        print(f"And it has max speed - {car.speed} mph")
    elif int(car.speed) < 45:
        print(f'It is {car.color}, but!')
        print('Do you think that bicycle is a car???')
        print(f"It has max speed - {car.speed} mph")
    else:
        print("IT'S NOT A CAR MATE!")
else:
    print("Something went wrong...")
    sys.exit("Error occured. \n Press F to pay respect. \n Restart script.")


