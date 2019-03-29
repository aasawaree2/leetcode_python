class Solutions:
    def firstBadVersion(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1

        if isBadVersion(mid):
            return mid
        else:
            return mid+1


def main():
    s = Solutions()
    print(s.firstBadVersion(10))


def isBadVersion(version):
    return api[version]


api = {1: False, 2: False, 3: False, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True}
if __name__ == '__main__':
    main()
