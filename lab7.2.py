all_words = set()
while True:
    line = input("Введіть рядок: ")
    if not line:
        break
    words = line.split()
    all_words.update(words)
result_string = " ".join(all_words)
print("Результат:", result_string)
