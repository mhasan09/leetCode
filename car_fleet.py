from typing import List

"""
        sort the start position.
        the car behind can only catch up no exceed.
        so if the car start late and speed is faster, it will catch up the car ahead of itself and they become a fleet.
        there is a target(or destination),so use arrive time to measure. 
        
        start late but arrive earlier means the car is behind and will catch up before arriving the destination.
        
        position  10  8  5  3  0
        distance  2   4  7  9  12
        speed.    2   4  1  3  1
        time.     1   1  7  3  12
                      ^     ^
                      |     |
                     catch  catch up the previous car before target, join the fleet
		stack = [1] , [1],[1,7],[1,7][1,7,12]
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        for pos, vel in sorted(zip(position, speed))[::-1]:

            dist = target - pos
            time = dist / vel

            if not stack:
                stack.append(time)

            elif time > stack[-1]:
                stack.append(time)

        return len(stack)


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
