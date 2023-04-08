central = 'C'
north = 'N'
north_east = 'NE'
east = 'E'
south_east = 'SE'
south = 'S'
south_west = 'SW'
west = 'W'
north_west = 'NW'
zelenogradskiy = 'Z'
troitskiy = 'T'
novomoskovskiy = 'N'

DIVISIONS = [
    (central, 'Центральный'),
    (north, 'Северный'),
    (north_east, 'Северо-Восточный'),
    (east, 'Восточный'),
    (south_east, 'Юго-Восточный'),
    (south, 'Южный'),
    (south_west, 'Юго-Западный'),
    (west, 'Западный'),
    (north_west, 'Северо-Западный'),
    (zelenogradskiy, 'Зеленоградский'),
    (troitskiy, 'Троицкий'),
    (novomoskovskiy, 'Новомосковский'),
]

DISTRICTS = [
    ('Medvedkovo', 'Медведково'),
    ('Butovo', 'Бутово'),
    ('Strogino', 'Строгино'),
    ('Dorogomilovo', 'Дорогомилово'),
    ('Otradnoye', 'Отрадное')

]

OBJ_TYPES = [
    ('liv_building', 'Индивидуальный жилой дом'),
    ('com_estate', 'Коммерческая недвижимость'),
    ('land', 'Земельный участок'),
    ('condo', 'Кондоминимум'),
]

CONDITIONS = [
    ('ok', 'Исправно'),
    ('dangerous', 'Авайрийное состояние'),
]

FIELD_TYPES = [
    ('I', 'Число'),
    ('S', 'Текст'),
    ('D', 'Дата'),
    ('B', 'Файл'),
]
