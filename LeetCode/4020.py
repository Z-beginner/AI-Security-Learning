from typing import List
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = 0
        floor = 0
        for request in requests:
            delta = request - floor
            floor = request
            if delta > 0:
                time += delta
            elif delta < 0:
                time -= delta
        return time