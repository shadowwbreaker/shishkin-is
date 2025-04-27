def substring_between_spaces(input_string):
    """

    Args:
        input_string (str):

    Returns:
        str:
    """
    try:
        if ' ' not in input_string:
            raise ValueError("Строка должна содержать хотя бы один пробел")

        first_space = input_string.find(' ')
        last_space = input_string.rfind(' ')

        if first_space == last_space:
            return ""

        return input_string[first_space + 1:last_space]
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return ""


input_str = "Test na probeli chek 1"
print(f"Исходная строка: '{input_str}'")
result = substring_between_spaces(input_str)
print(f"Результирующая подстрока: '{result}'")