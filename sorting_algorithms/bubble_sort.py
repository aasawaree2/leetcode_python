# Bubble Sort - Swap adjacent element if not in order.
# In each pass the last element is the largest amongst the current set of elements.


class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def sort2(self, arr):
        # Optimized bubble sorted
        # If flag was changed means there was a swap, so continue.
        # If flag was not changed means its sorted so no need to continue further.
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break
        return arr


def main():
    b = BubbleSort()
    print(b.sort([1, 4, 3, 1, 2]))
    print(b.sort2([1, 4, 3, 1, 2]))


if __name__ == '__main__':
    main()

