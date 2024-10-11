input_string = input("Введіть рядок: ")
words = input_string.split()
if len(words) > 2:
    output_string = words[0] + " " + words[-1]
else:
    output_string = input_string
print("Результат:", output_string)
