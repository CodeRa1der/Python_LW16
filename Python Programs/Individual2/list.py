# Individual2/list.py

def list_of_routes(roadway):
    if roadway:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 14,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^5} | {:^20} | {:^20} |'.format(
               "Номер маршрута",
                "Место отправки",
                "Место прибытия"
            )
        )
        print(line)
        # Вывод данных о маршрутах
        for number, route in enumerate(roadway, 1):
            print(
                '| {:<14} | {:<20} | {:<20} |'.format(
                    number,
                    route.get('first', ''),
                    route.get('second', '')
                )
            )
            print(line)
    else:
        print("Список маршрутов пуст")
