"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

"""
class Matrix:
    def __init__(self, lists):
        self.lists = lists
    def __str__(self):
        return '\n'.join([''.join(map(str,line)) for line in self.lists])
    def __add__(self, other):
        answer = ''
        if len(self.lists) == len(other.lists):
            for line_1, line_2 in zip(self.lists, other.lists):
                if len(line_1) != len(line_2):
                    return 'Проблеммы с формой'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Проблеммы с формой'
        return answer

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print(matrix_2)
print()
print(matrix_1 + matrix_2)