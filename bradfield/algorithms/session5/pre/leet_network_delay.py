# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
#
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.

import heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph: object = collections.defaultdict(list)
        distances = {}
        distances[starting_vertex] = 0

        entry_lookup = {}
        pq = [(0, K)]

        for u, v, w in times:
            entry = (v, w)
            heapq.heappush(pq, entry)

