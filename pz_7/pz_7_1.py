def insert_string_before_char(C, S, S0):
    """
    Args:
        C (str):
        S (str):
        S0 (str):

    Returns:
        str:
    """
    try:
        if len(C) != 1:
            raise ValueError("C должен быть одним символом")

        result = []
        for char in S:
            if char == C:
                result.append(S0)
            result.append(char)
        return ''.join(result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return S


C = 'a'
S = "banana"
S0 = "XYZ"
print(f"Исходная строка: {S}")
result = insert_string_before_char(C, S, S0)
print(f"Результирующая строка: {result}")