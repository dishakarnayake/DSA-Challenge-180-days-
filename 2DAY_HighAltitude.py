# Approach 1: Using a simple loop [ brute force method]

class Solution:
    def largestAltitude(self, gain):
       
        max_altitude = 0
        current_altitude = 0
        for i in range(len(gain) + 1):
            if i > 0:
                current_altitude += gain[i - 1]
                max_altitude = max(max_altitude, current_altitude)
        return max_altitude

obj = Solution()
gain = [-5,1,5,0,-7]    
max_ALtitude  = obj.largestAltitude(gain)   
print(max_ALtitude) 




# Approach 2: Using the max function with a generator expression[Optimal approach]

def highestAltitude(gain):
    max_altitude = 0
    current_altitude = 0
    for gain_in_altitude in gain:
        current_altitude += gain_in_altitude
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude
        