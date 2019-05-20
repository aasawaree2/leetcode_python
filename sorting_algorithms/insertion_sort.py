class InsertionSort:
    def sort(self, arr):
        length = len(arr)

        for i in range(1, length):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr


def main():
    b = InsertionSort()
    print(b.sort([1, 3, 5, 2, 7, 4, 2]))


if __name__ == '__main__':
    main()
