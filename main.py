#Задача 1 (просто) "Арифметика"

print("1st program")
result = (9 ** 0.5) * 5
print(result)

#Задача 2 (просто) "Логика"

print("2nd program")
result2 = 9.99 > 9.98 and 1000 != 1000.1
print(result2)

#Задача 3 (средне) "Школьная загадка"

result3 = "2 * 2 + 2"
print(result3)

result4 = "2 * (2 + 2)"
print(result2)

comparison_result = result4 == result4
print(comparison_result)

#Задача 4 (сложно) "Первый после точки"

number_str = '123.456'

number_float = float(number_str)
shifted_number = number_float * 10
integer_part = int(shifted_number)
first_digit_after_point = integer_part % 10

print(first_digit_after_point)