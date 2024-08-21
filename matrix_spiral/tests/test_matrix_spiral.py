import asyncio
from matrix_spiral import get_matrix, traverse_matrix_spiral

# URL-адрес, по которому находится текстовое представление матрицы
URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

# Ожидаемый результат обхода матрицы по спирали
expected_response = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]

def test_get_matrix():
    """
    Тестирует функцию get_matrix.
    """
    assert asyncio.run(get_matrix(URL)) == expected_response

def test_traverse_matrix_spiral():
    """
    Тестирует функцию traverse_matrix_spiral. Исходная матрица 5х5.
    """
    matrix = [
        [10, 20, 30, 40, 50],
        [60, 70, 80, 90, 100],
        [110, 120, 130, 140, 150],
        [160, 170, 180, 190, 200],
        [210, 220, 230, 240, 250]
    ]
    expected_response = [
        10, 60, 110, 160, 210,
        220, 230, 240, 250, 200,
        150, 100, 50, 40, 30,
        20, 70, 120, 170, 180,
        190, 140, 90, 80, 130
    ]
    result = traverse_matrix_spiral(matrix)
    assert result == expected_response

def test_traverse_matrix_spiral_small():
    """
    Тестирует функцию traverse_matrix_spiral. Исходная матрица 2х2.
    """
    matrix = [
        [11, 22],
        [33, 44]
    ]
    expected = [11, 33, 44, 22]
    result = traverse_matrix_spiral(matrix)
    assert result == expected

def test_traverse_matrix_spiral_single():
    """
    Тестирует функцию traverse_matrix_spiral. Исходная матрица 1х1.
    """
    matrix = [[100]]
    expected = [100]
    result = traverse_matrix_spiral(matrix)
    assert result == expected

if __name__ == "__main__":
    # Запускаем все тесты и выводим сообщение, если все тесты пройдены успешно
    test_get_matrix()
    test_traverse_matrix_spiral()
    test_traverse_matrix_spiral_small()
    test_traverse_matrix_spiral_single()
    print("All tests completed successfully!")
