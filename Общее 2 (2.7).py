
str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
simb = set(str1) & set(str2)
if simb:
    print("Общие символы: " + "".join(simb))
else:
    print("Общих символов нет")