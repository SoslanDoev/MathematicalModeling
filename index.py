import numpy as np
import os

# Функция для очистки экрана, чтобы код выглядел более "чисто"
def clear_screen(): 
    os.system("cls")

# Основное приложение
def application():
    # Функция для проверки, что общие затраты не превышают общий выпуск
    def verify_total_input(A_matrix, X_vector):
        total_costs = A_matrix.dot(X_vector)
        return np.all(total_costs <= X_vector)

    # Ввод количества отраслей
    num_industries = int(input("Введите количество отраслей: "))
    
    # Ввод матрицы коэффициентов затрат
    coefficient_matrix = []
    for row in range(num_industries):
        temp_row = []
        for col in range(num_industries):
            while True:
                # Ввод данных с проверкой на отрицательные значения
                user_input = float(input(f"Введите коэффициент (строка: {row}, столбец: {col}): "))
                if user_input < 0:
                    print("Ошибка! Коэффициент не может быть отрицательным.")
                    continue
                temp_row.append(user_input)
                break
        coefficient_matrix.append(temp_row)

    # Преобразуем матрицу затрат в формат numpy для удобных вычислений
    A_matrix = np.array(coefficient_matrix, dtype=np.float64)
    
    # Проверка, что сумма коэффициентов по строкам не превышает 1
    for row in range(num_industries):
        row_sum = 0
        for col in range(num_industries):
            row_sum += A_matrix[row][col]
        if row_sum > 1:
            print(f"Ошибка: сумма строки {row+1} больше 1.")
            return

    # Проверка, что сумма коэффициентов по столбцам больше 1
    column_flag = False
    for col in range(num_industries):
        col_sum = 0
        for row in range(num_industries):
            col_sum += A_matrix[row][col]
        if col_sum < 1:
            column_flag = True
            break
    if not column_flag:
        print("Ошибка: сумма по столбцам должна быть меньше 1.")
        return 

    # Ввод вектора конечного потребления
    Y_vector = []
    for index in range(num_industries):
        consumption_input = float(input(f"Введите конечное потребление для отрасли {index}: "))
        Y_vector.append(consumption_input)

    # Проверка, что затраты не превышают выпуск
    if verify_total_input(A_matrix, Y_vector):
        print("Проверка успешна: затраты не превышают выпуск.")
    else:
        print("Ошибка: затраты превышают выпуск.")
        return

    # Создание единичной матрицы
    identity_matrix = []
    for i in range(num_industries):
        temp_row = []
        for j in range(num_industries):
            if i == j:
                temp_row.append(1)
            else:
                temp_row.append(0)
        identity_matrix.append(temp_row)
    
    # Преобразуем единичную матрицу в numpy массив
    E_matrix = np.array(identity_matrix, dtype=np.float64)

    # Вывод промежуточных данных для отладки
    print("Матрица A: \n", A_matrix)
    print("Вектор конечного потребления Y: \n", Y_vector)
    print("Единичная матрица E: \n", E_matrix)

    # 1) Вычисление разности E - A
    matrix_diff = np.subtract(E_matrix, A_matrix)
    print("E - A: \n", matrix_diff)

    # 2) Решение уравнения (E - A)^-1 * Y = X
    solution_vector = np.linalg.solve(matrix_diff, Y_vector)
    print("Решение для X: \n", solution_vector)

# Запуск программы
if __name__ == "__main__":
    clear_screen()  # Очищаем экран при запуске
    application()   # Запуск основной функции