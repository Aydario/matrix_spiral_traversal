import aiohttp
import asyncio
from typing import List

async def get_matrix(url: str) -> List[int]:
    """
    Асинхронно выполняет HTTP GET-запрос к указанному URL, получает текстовое представление матрицы,
    преобразует двумерный список целых чисел и возвращает список элементов матрицы (который обошли
    по спирали против часовой стрелки, начиная с левого верхнего угла).

    Args:
        url (str): URL-адрес, по которому находится текстовое представление матрицы.

    Returns:
        List[int]: Список целых чисел, представляющих элементы матрицы, обходящиеся 
                   по спирали против часовой стрелки, начиная с левого верхнего угла.
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status >= 500:
                    raise Exception(f'Server error: HTTP {response.status}')
                if response.status != 200:
                    raise Exception(f'Failed to fetch matrix: HTTP {response.status}')
                matrix_text = await response.text()
                matrix = format_matrix(matrix_text.strip())
                return traverse_matrix_spiral(matrix)
        except aiohttp.ClientError as e:
            raise Exception(f'Network error: {e}')
        except asyncio.TimeoutError:
            raise Exception('Request timed out')
        

def format_matrix(matrix_text: str) -> List[List[int]]:
    """
    Форматирует текстовое представление матрицы в двумерный список целых чисел.
    Args:
        matrix_text (str): Текстовое представление матрицы.
    Returns:
        List[List[int]]: Двумерный список целых чисел, представляющий матрицу.
    """
    text = matrix_text.split('\n')
    res = []
    for i in range(1, len(text), 2):
        res.append(list(map(lambda x: int(x.strip()), text[i].strip('| ').split('|'))))
    return res
        

def traverse_matrix_spiral(matrix: List[List[int]]) -> List[int]:
    """
    Обходит матрицу по спирали против часовой стрелки, начиная с левого верхнего угла.
    Args:
        matrix (List[List[int]]): Двумерный список целых чисел, представляющий матрицу.
    Returns:
        List[int]: Список целых чисел, представляющих элементы матрицы, обходящиеся 
                   по спирали против часовой стрелки, начиная с левого верхнего угла.
    """
    result = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix) if matrix else 0

    while top < bottom and left < right:
        # Сверху вниз по левому столбцу
        for i in range(top, bottom):
            result.append(matrix[i][left])
        left += 1
        # Слева направо по нижней строке
        for i in range(left, right):
            result.append(matrix[bottom - 1][i])
        bottom -= 1

        if left < right:
            # Снизу вверх по правому столбцу
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][right - 1])
            right -= 1

        if top < bottom:
            # Справа налево по верхней строке
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[top][i])
            top += 1

    return result
    