def main():
    test_data = [1, 2, 3, 4, 5]
    arr_len = len(test_data)
    print(arr_len)

    for i in range(arr_len - 1):
        for j in range(arr_len - 1):
            if test_data[i] > test_data[j + 1]:
                temp = test_data[i]
                test_data[i] = test_data[j + 1]
                test_data[j + 1] = temp

    for i in range(arr_len):
        print(test_data[i])


if __name__ == '__main__':
    main()
