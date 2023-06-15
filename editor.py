def display_menu():
    """Отображает меню редактора"""
    print("Текстовый редактор")
    print("1. Открыть файл")
    print("2. Сохранить файл")
    print("3. Добавить текст")
    print("4. Вывести текст")
    print("5. Выход")

def open_file():
    """Открывает файл и читает его содержимое"""
    filename = input("Введите имя файла для открытия: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Файл успешно открыт.")
            return content
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Ошибка при открытии файла:", e)
    return None

def save_file(content):
    """Сохраняет содержимое в файл"""
    filename = input("Введите имя файла для сохранения: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("Файл успешно сохранен.")
    except Exception as e:
        print("Ошибка при сохранении файла:", e)

def add_text(content):
    """Добавляет текст в текущее содержимое"""
    new_text = input("Введите текст для добавления: ")
    content += new_text
    print("Текст успешно добавлен.")
    return content

def display_text(content):
    """Выводит текущее содержимое текста"""
    print("Текущее содержимое:")
    print(content)

# Основная часть программы
text_content = ""

while True:
    display_menu()
    choice = input("Выберите опцию (1-5): ")

    if choice == "1":
        text_content = open_file()
    elif choice == "2":
        save_file(text_content)
    elif choice == "3":
        text_content = add_text(text_content)
    elif choice == "4":
        display_text(text_content)
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
