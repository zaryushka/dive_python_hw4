# Напишите функцию для транспонирования матрицы

def transp_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    new_matrix = [[0 for i in range(rows)] for j in range(columns)]
    
    for i in range(rows):
        for j in range(columns):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix
                  
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = transp_matrix(matrix)
for row in new_matrix:
    print(row)

