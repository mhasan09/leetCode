import random
import string
from datetime import datetime


def generate_names(num):
    a_list = list()
    a_dict = dict()
    id = 0

    for i in range(num):
        random_name = "".join([
            random.choice(string.ascii_letters)
            for j in range(7)
        ])
        id += random.randint(1, 5)
        a_list.append({
            "id": id,
            "name": random_name,
            "age": random.randint(1, 100),
        })
        a_dict[id] = {
            "id": id,
            "name": random_name,
            "age": random.randint(1, 100),
        }
    return a_list, a_dict


my_list, my_dict = generate_names(1000000)
the_id = my_list[-1]["id"]
if __name__ == '__main__':
    my_list, my_dict = generate_names(1000000)
    the_id = my_list[-1]["id"]
    time_1 = datetime.now()
    right_persons = [
        person
        for person in my_list
        if person["id"] == the_id
    ]
    time_2 = datetime.now()
    print("Found!", right_persons)
    print("Time taken:", (time_2 - time_1).total_seconds(), "sec")
