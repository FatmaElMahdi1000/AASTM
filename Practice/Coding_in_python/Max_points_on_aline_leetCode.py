class Solution:
    def maxPoints(self, points) :
        max_line_points = []
        if len(points) <= 2:
            return len(points)
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i] #forming a tuple
                x2, y2 = points[j] #forming a tuple
                current_line = []
                for p in points:
                    x, y = p
                    if ((x2 - x1) *(y-y1) == (y2 - y1)*(x-x1)):
                        current_line.append(p)
                if len(current_line) > len(max_line_points):
                    max_line_points = current_line
        return len(max_line_points)


points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
res = Solution()
Final = res.maxPoints(points)
print(Final)