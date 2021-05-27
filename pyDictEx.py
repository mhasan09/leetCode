# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# x = dict(zip(keys,values))
#
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# z = {**dict1, **dict2}
#
#
#
# sampleDict = {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# xx = sampleDict['class']['student']['marks']['history']
#
#
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# resDict = dict.fromkeys(employees, defaults)
#
# sampleDict2 = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# keys = ["name", "salary"]
# kk = {k:sampleDict2[k] for k in keys}
# print(kk)
#
#
# sampleDict3 = {'string': 100, 'b': 200, 'c': 300}
# print(200 in sampleDict3.values())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat1 = Cat('Andy', 2)
cat1.info()