class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacencyList = {}
        for i in range(numCourses):
            adjacencyList[i] = []

        for req in prerequisites:
            adjacencyList[req[0]].append(req[1])
        
        visited = set()
        visiting = set()

        res = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                visited.add(course)
                return True
            if adjacencyList[course] == []:
                res.append(course)
                visited.add(course)
                return True

            visiting.add(course)
            for c in adjacencyList[course]:
                if not dfs(c):
                    return False
            visiting.remove(course)
            visited.add(course)

            res.append(course)
    
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res