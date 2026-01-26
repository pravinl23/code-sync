class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        LOPS = [] # [position, speed]
        for i in range(len(position)):
            LOPS.append([position[i], speed[i]])
        LOPS.sort(key = lambda x: x[0], reverse = True)

        stack = []
        for i in range(len(position)):
            spd = LOPS[i][1]
            pos = LOPS[i][0]

            time = float(target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)