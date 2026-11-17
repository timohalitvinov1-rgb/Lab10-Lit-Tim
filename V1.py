def rot_mat_90(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list)for row in matrix):
        raise ValueError("неккоректные данные")

    if matrix and len({len(row) for row in matrix}) != 1:
        raise ValueError("Матрица не квадратна")

    return [list(row) for row in zip(*matrix[::-1])] 


assert rot_mat_90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
assert rot_mat_90([[1]]) == [[1]]
assert rot_mat_90([]) == []
assert rot_mat_90([[1, 2]]) == [[1], [2]]

a = [[1,2], [3, 4]]
rot_mat_90(a)
assert a == [[1, 2], [3,4]]

try:
    rot_mat_90([1,2])
except ValueError:
    pass