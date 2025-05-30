def logging(func):
    def log_function_called():
        print(f'{func} called.')
        func()
    return log_function_called


@logging
def recreate_without_dublicates():
    new_list = [1,1,7,2,2,8,3,3,9,4,4,10,5,5,11,6,6]
    new_list = list(set(new_list))
    print(new_list)

@logging
def sort_lists():
    my_list = [9,4,6,3,7,5,2,8]
    my_list = sorted(my_list)
    print(my_list)

@logging
def create_sort():
    a = int(input("Введите начальное число списка: "))
    b = int(input("Введите следующее за конечным число списка: "))
    c = int(input("Введите шаг добавления чисел списка: "))
    my_third_list = list(range(a, b, c))
    print(f'Ваш список: {my_third_list}')

recreate_without_dublicates()
sort_lists()
create_sort()