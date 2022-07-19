# Напишите функцию, которая проверяет: является ли слово палиндромом
def polind(word):
    if str(word)==str(word)[::-1]:
        print("полиндром: ",(word))
    else:
        print("неполиндром: ",(word))

polind('кок')
polind('кот')