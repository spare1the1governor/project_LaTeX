def create_latex_document(title, author, date, office, section, subsection, text ):
    # Читаем шаблон
    with open('professor.tex', 'r', encoding='utf-8') as file:
        document = file.read()

    # Заменяем метки в шаблоне на переданные значения
    document = document.replace('TITLE', title)
    document = document.replace('AUTHOR', author)
    document = document.replace('DATE', date)
    document = document.replace('NAME, CITY', office)
    document = document.replace('SECTION', section)
    document = document.replace('U', subsection)
    document = document.replace('Main text', text)

    # Записываем новый файл с заполненным шаблоном
    with open('generated_document.tex', 'w', encoding='utf-8') as file:
        file.write(document)

    print("LaTeX документ успешно создан: generated_document.tex")


# Пример вызова функции
title = input('Заголовок: ')
author = input('Автор: ')
date = input('Дата: ')
office = input('Название и город издательства: ')

section = input('Раздел: ')
subsection = input('Подраздел: ')

text = input('Основной текст: ')

# Разбиваем текст на список слов
l_text = list(text.split(" "))

# Проходим по каждому слову и выполняем нужную замену
i = 0
while i < len(l_text): 
    if l_text[i] == 'green':  # Если нашли слово 'green'
        if i + 1 < len(l_text):
            l_text[i] = '{\\' + l_text[i] + ' ' + l_text[i+1] + '}'
            # Удаляем следующее слово из списка, так как оно уже добавлено в фигурные скобки
            del l_text[i+1]
        i += 1  # Переходим к следующему слову
    else:
        i += 1  # Просто двигаемся по списку

# Возвращаем изменённую строку
modified_text = " ".join(l_text)

# Вызов функции для создания LaTeX документа
create_latex_document(title, author, date, office, section, subsection, modified_text)

