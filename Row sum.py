def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the matrix elements:")
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input()))
        matrix.append(row)
    rowSum = get_row_sum(matrix)
    print("Row-wise sums:", end=" ")
    for sum in rowSum:
        print(sum, end=" ")

def get_row_sum(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    rowSum = [0] * rows
    for j in range(columns):
        sum = 0
        for i in range(rows):
            sum += matrix[i][j]
        rowSum[j] = sum
    return rowSum

if __name__ == "__main__":
    main()
