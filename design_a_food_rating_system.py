import heapq
from collections import defaultdict
from typing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating = {}
        self.cuisines = defaultdict(list)
        self.food_cuisine = {}

        for i in range(len(foods)):
            food, r, cuisine = foods[i], ratings[i], cuisines[i]
            self.rating[food] = -r
            self.food_cuisine[food] = cuisine
            heapq.heappush(self.cuisines[cuisine], (-r, food))

        """
        rating = {'kimchi': -9, 'miso': -12, 'sushi': -8, 'moussaka': -15, 'ramen': -14, 'bulgogi': -7}
        cuisines = defaultdict(<class 'list'>, {'korean': [(-9, 'kimchi'), (-7, 'bulgogi')], 'japanese': [(-14, 'ramen'), (-8, 'sushi'), (-12, 'miso')], 'greek': [(-15, 'moussaka')]})
        food_cuisine = {'kimchi': 'korean', 'miso': 'japanese', 'sushi': 'japanese', 'moussaka': 'greek', 'ramen': 'japanese', 'bulgogi': 'korean'}
        
        """

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = -newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.rating[self.cuisines[cuisine][0][1]] != self.cuisines[cuisine][0][0]:
            heapq.heappop(self.cuisines[cuisine])

        return self.cuisines[cuisine][0][1]


obj = FoodRatings(["kimchi","miso","sushi","moussaka","ramen","bulgogi"], ["korean","japanese","japanese","greek","japanese","korean"],
                  [9,12,8,15,14,7])
obj.changeRating("sushi",16)
param_2 = obj.highestRated("japanese")