class Solutions:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))
        v1_len = len(version1)
        v2_len = len(version2)

        for i in range(max(v1_len, v2_len)):
            v1 = version1[i] if i < v1_len else 0
            v2 = version2[i] if i < v2_len else 0
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0


def main():
    s = Solutions()


if __name__ == '__main__':
    main()