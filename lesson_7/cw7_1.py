class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix


    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=" ")
            print("")
        return ""

    def __add__(self, other):
        new_mtx = []
        for i in range(len(self.matrix)):
            new_mtx.append([])
            for j in range(len(self.matrix[i])):
                new_el = self.matrix[i][j] + other.matrix[i][j]
                new_mtx[i].append(new_el)
        return Matrix(new_mtx)


mtx_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mtx_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
mtx_3 = Matrix([[1, 2, 3], [3, 2, 1], [1, 2, 3]])
print(mtx_1 + mtx_2 + mtx_3)
