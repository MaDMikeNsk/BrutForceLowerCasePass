import itertools as it
import string


def tuple_to_string(tup):
    res = ''
    for item in tup:
        res += str(item)
    return res


def brut(password_length: int, correct_password: str) -> str:
    print(f'Подождите, идёт подбор пароля из {password_length} символов...')
    char_string = string.ascii_lowercase  # Пароль состоит из маленьких англ букв
    combination = it.product(char_string, repeat=password_length)  # Размещения с повторениями (iterator) type: tuple

    i = 0
    for i in range(1, len(char_string) ** password_length + 1):
        temp_comb = next(combination)
        if tuple_to_string(temp_comb) == correct_password:
            return f'Пароль "{tuple_to_string(temp_comb)}" найден за {i} итерации(й)'
    return f'Пароль не найден, итераций {i}'


a = brut(4, 'z1zz')
print(a)
