import argparse

def main():
    # Создание парсера аргументов
    parser = argparse.ArgumentParser(description='Обработка числа и строки с опциями.')
    parser.add_argument('number', type=int, help='Число для вывода')
    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')

    # Проверка аргументов
    args = parser.parse_args(['42', 'Пример строки', '--verbose', '--repeat', '3'])


    # Если включён verbose, выводим дополнительные данные
    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text="{args.text}", repeat={args.repeat}')

    # Повторение строки
    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')

if __name__ == '__main__':
    main()


