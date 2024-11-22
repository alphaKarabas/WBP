from src.Bottle import Bottle

def load_bottles(load_image, water_levels={'8': 0, '5': 0, '3': 0}):
    """Функция для загрузки данных бутылок."""
    return {
        '8': Bottle(
            '8',
            (50, 273),
            8,
            {
                'shadow': (load_image('8l_shadow.png'), (8, 215)),
                'bottle': (load_image('8l_bottle.png'), (0, 0)),
                'water': (load_image('8l_water.png'), {
                    1: (5, 211),
                    2: (5, 197),
                    3: (5, 182),
                    4: (5, 167),
                    5: (5, 153),
                    6: (5, 137),
                    7: (5, 122),
                    8: (5, 106),
                }),
                'scale': (load_image('8l_scale.png'), (40, 120)),
            },
            water_levels['8']
        ),
        '5': Bottle(
            '5',
            (250, 308),
            5,
            {
                'shadow': (load_image('5l_shadow.png'), (-2, 185)),
                'bottle': (load_image('5l_bottle.png'), (0, 0)),
                'water': (load_image('5l_water.png'), {
                    1: (4, 172),
                    2: (4, 152),
                    3: (4, 132),
                    4: (4, 111),
                    5: (4, 90),
                }),
                'scale': (load_image('5l_scale.png'), (35, 100)),
            },
            water_levels['5']
        ),
        '3': Bottle(
            '3',
            (450, 357),
            3,
            {
                'shadow': (load_image('3l_shadow.png'), (0, 140)),
                'bottle': (load_image('3l_bottle.png'), (0, 0)),
                'water': (load_image('3l_water.png'), {
                    1: (4, 124),
                    2: (4, 100),
                    3: (4, 72),
                }),
                'scale': (load_image('3l_scale.png'), (25, 80)),
            },
            water_levels['3']
        ),
    }