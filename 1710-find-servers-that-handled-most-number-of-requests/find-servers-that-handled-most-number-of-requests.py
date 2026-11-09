from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release servers whose requests are completed
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            # No server is available
            if not available:
                continue

            # Find the first available server >= i % k
            target = i % k
            idx = available.bisect_left(target)

            # Wrap around if necessary
            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request to server
            count[server] += 1

            # Add server to busy heap
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        max_requests = max(count)

        return [
            i for i in range(k)
            if count[i] == max_requests
        ]
