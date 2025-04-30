def is_happy_ticket(string):
    if len(string) % 2 == 0:
        half_1 = string[0:(len(string) // 2)]
        half_2 = string[(len(string) // 2):]
        sum_1 = 0
        sum_2 = 0
        for number in half_1:
            sum_1 = sum_1 + int(number)
        for number in half_2:
            sum_2 = sum_2 + int(number)
        if sum_1 == sum_2:
            return True
        else:
            return False
    else:
        return False

# Проверка

string = '385916'

print(is_happy_ticket(string))