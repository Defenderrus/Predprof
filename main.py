"""Считывание данных из файла vacancy.csv и запись в переменную data"""
with open("vacancy.csv", encoding="utf8") as file:
    data = [line.strip().split(";") for line in file.readlines()][1:]

    """Обработка данных (задание 1)
       Переменная ans собирает нужные данные"""
    ans = []
    for s, w, cs, r, c in data:
        """Переменные s, w, cs, r, c - заголовки столбцов по первой букве слова"""
        ans.append([int(s), r, c])
    ans.sort()

    """Запись данных в файл vacancy_new.csv"""
    with open("vacancy_new.csv", "w", encoding="utf8") as file_new:
        file_new.write("company;role;Salary\n")
        for j in ans[:-4:-1]:
            j = list(map(str, j))
            file_new.write(";".join(j[::-1])+"\n")

    """Сортировка данных по кол-ву сотрудников в компании (задание 2)"""
    for i in range(len(data)-1):
        """Переменная ind хранит индекс минимального элемента minimum"""
        ind, minimum = 0, 10**9
        for j in range(i+1, len(data)):
            if int(data[j][2]) < minimum:
                minimum = int(data[j][2])
                if int(data[i][2]) > minimum:
                    ind = j
        """Обмен данными"""
        if ind:
            data[i], data[ind] = data[ind], data[i]

    """Обработка и вывод данных"""
    for s, w, cs, r, c in data:
        """Переменные s, w, cs, r, c - заголовки столбцов по первой букве слова"""
        if r == "классный руководитель":
            print(f"В компании {c} есть заданная профессия: {r}, "f"з/п в такой компании составит: {s}")
            break

    """Получение данных с консоли и запись в переменную line (Задание 3)"""
    line = input()
    """Зацикливание программы, стоп-слово 'None'"""
    while line != "None":

        """Поиск вакансий"""
        array = []
        """Переменная array хранит вакансии"""
        for s, w, cs, r, c in data:
            """Переменные s, w, cs, r, c - заголовки столбцов по первой букве слова"""
            if line == c:
                array.append([r, s])

        """Вывод данных в консоль"""
        if array:
            for r, s in array:
                print(f"В {line} найдена вакансия: {r}. З/п составит: {s}")
        else:
            print("К сожалению, ничего не удалось найти")

        """Ожидание новых данных"""
        line = input()
