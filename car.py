class Car :
    car_type = "unknown"
    car_types = ('sports_car', 'usual_car', 'not_a_car')
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

# choosing car type method
    @classmethod
    def choose_type(cls, speed):
        if (120 < int(speed) < 300):
            cls.car_type = cls.car_types[0]
        elif (45 < int(speed) < 120):
            cls.car_type = cls.car_types[1]
        else:
            cls.car_type = cls.car_types[2]

car = Car(input("Choose color: "),input("Choose max speed (in mph): "))

car.choose_type(car.speed)

if (car.car_type == "sports_car"):
    print("This is fast car!")
elif (car.car_type == "usual_car"):
    print("Good car, mate!")
elif (car.car_type == "not_a_car"):
    print("IT'S NOT A CAR MATE!")
else:
    print("Something went wrong...")

#try:

#except:
#    fdsgsd
#raise ValueError
#finally:
print(f'{car.speed} mph')
#car.car_type