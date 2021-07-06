while True:
    filename = input("Введите название файла: ")
    text = input("Ваши личные данные: ")

    data = open('lesson05_data/' + filename, "w")
    data.write(text)
    data.close()
