class Solutions:
    def rotate(self, matrix) -> None:
        matrix.reverse()
        print(matrix)
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


def main():
    s = Solutions()
    s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


if __name__ == '__main__':
    main()
