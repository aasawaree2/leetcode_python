import heapq


class Solutions:
    def kClosest(self, points, K):
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]

    def kClosest2(self, points, K):
        heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > K:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


def main():
    s = Solutions()
    a = s.kClosest([[1, 3], [-2, 2]], 1)
    print(a)
    a = s.kClosest([[1, 3], [-2, 2]], 1)
    print(a)


if __name__ == '__main__':
    main()
