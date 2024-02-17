#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from add import add_route
from list import list_of_routes
from help import help
from exit import exit_program

def main():
    # Список маршрутов
    routes = []
    # Начало бесконечного цикла команд
    while True:
        # Сюда вписывать команды
        command = input('>>> ').lower()

        # Команда help
        if command == 'help':
            help()

        # Команда add
        elif command == 'add':
            route = add_route()
            # Добавление словаря в список
            routes.append(route)

        # Команда list
        elif command == 'list':
            list_of_routes(routes)

        # Команда exit
        elif command == 'exit':
            exit_program()

        # Другая команда/неверно введенная команда
        else:
            print(f'Неизвестная команда {command}')

if __name__ == '__main__':
    main()
