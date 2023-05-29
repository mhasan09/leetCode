class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def add_car(self, car_type: int) -> bool:
        if car_type == 1 and self.big > 0:
            self.big -= 1
            return True
        elif car_type == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif car_type == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
param_1 = obj.add_car(1)
param_2 = obj.add_car(2)
param_3 = obj.add_car(3)
