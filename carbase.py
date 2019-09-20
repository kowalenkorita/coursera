import csv
import os

class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand,photo_file_name,carrying)
        self.car_type = "truck"

        if body_whl is not "":
            self.body_width = float(body_whl.split("x")[0])
            self.body_height = float(body_whl.split("x")[1])
            self.body_length = float(body_whl.split("x")[2])
        else:
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0

    def get_body_volume(self):
        return self.body_width*self.body_height*self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand,photo_file_name,carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_type = row[0]
                if car_type == "car":
                    car = Car(brand=row[1], photo_file_name=row[3], carrying=row[5], passenger_seats_count=row[2]) 
                    car_list.append(car)
                elif car_type == "truck":
                    # создание экземпляра Truck
                    truck = Truck(brand=row[1], photo_file_name=row[3], carrying=row[5], body_whl=row[4]) 
                    car_list.append(truck)
                elif car_type == "spec_machine":
                    # создание экземпляра spec_machine
                    spec_machine = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6]) 
                    car_list.append(spec_machine)
                # print(row)
            except IndexError:
                continue

    return car_list