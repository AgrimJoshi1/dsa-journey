# 1344. Angle Between Hands of a Clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_h = 30 * hour + 0.5 * minutes
        angle_min = 6 * minutes

        

        angle = abs(angle_h - angle_min)

        return min(angle, 360 - angle)
#Approach
#Simple maths formula
