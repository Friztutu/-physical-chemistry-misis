"""
Спроектировать защитное заземление оборудования лаборатории, находящейся в [climate_zone]
климатической зоне. Заземляющее устройство заглублено на глубину [depth] м. Грунт – [soil].
Для вертикальных заземлителей длиной lc = [vertical_length] м использовать стальные трубы диаметром
d = [diameter] мм. Для соединительной полосы использовать стальную шину сечением [width] х 4 мм.
Заземлители расположить в ряд. Источник тока (трансформатор) мощностью [power] кВ·А подает
напряжение в лабораторию [voltage] В.
"""

import math


# Определим нормативное значение сопротивления заземления Rн
def main(power_db=400, soil_db='суглинок', climate_zone_db='2', scheme_db='в ряд'):
    depth = 0.8
    vertical_length = 3.0
    diameter = 40 / 1000
    width = 40 / 1000
    voltage = 400
    power = power_db
    soil = soil_db
    climate_zone = climate_zone_db
    scheme = scheme_db
    return calculate(depth, vertical_length, diameter, width, voltage, power, soil, climate_zone, scheme)


def find_middle_value(quantity, grounding_multipliers):
    quantities = sorted(list(grounding_multipliers.keys()) + [quantity])
    current_index = quantities.index(quantity)

    return grounding_multipliers[quantities[current_index - 1]] + (
            grounding_multipliers[quantities[current_index + 1]]
            - grounding_multipliers[
                quantities[current_index - 1]]) / 2


def calculate(depth, vertical_length, diameter, width, voltage, power, soil, climate_zone, scheme):
    if voltage < 1000:
        normative_resistance = 4 if power < 100 else 10
    else:
        normative_resistance = 10 if power < 500 else 0.5

    soil_resistance_tabular = {"глина": 40, "суглинок": 100, "чернозем": 200,  # таблица 5.1
                               "супесок": 300, "песок": 700, "скалистый": 2000}

    climate_multipliers = {"1": (2.0, 7.0), "2": (1.8, 4.5), "3": (1.6, 2.5), "4": (1.4, 2.0)}  # таблица 5.2

    vertical_value = soil_resistance_tabular[soil] * climate_multipliers[climate_zone][0]  # pc расч
    horizontal_value = soil_resistance_tabular[soil] * climate_multipliers[climate_zone][1]  # pп расч

    # Определим сопротивление одиночного вертикального заземлителя с учетом удельного сопротивления грунта

    h = depth + vertical_length / 2

    single_vertical_resistance = (vertical_value / (2 * math.pi * vertical_length)) * \
                                 (math.log(2 * vertical_length / diameter) +
                                  1 / 2 * math.log((4 * h + vertical_length) / (4 * h - vertical_length)))  # Rc

    # Учитывая норму сопротивления заземления Rн, определим число вертикальных
    # заземлителей без учета взаимного экранирования
    num_inaccurate = math.ceil(single_vertical_resistance / normative_resistance)

    # Определим конечное число вертикальных заземлителей и их сопротивление без учёта соединительной полосы
    # При расположении в ряд η = 2, при расположении по контуру η = 3

    if scheme == "в ряд":
        vert_grounding_multipliers = {2: 0.91, 3: 0.86, 4: 0.83, 5: 0.8, 6: 0.77, 10: 0.74, 20: 0.67}  # таблица 5.3
        eta = 2  # η
    else:
        vert_grounding_multipliers = {4: 0.85, 6: 0.80, 10: 0.76, 20: 0.71, 40: 0.66, 60: 0.64, 100: 0.62}
        eta = 3

    if num_inaccurate not in vert_grounding_multipliers:
        vert_grounding_multipliers[num_inaccurate] = find_middle_value(num_inaccurate, vert_grounding_multipliers)

    num_accurate = math.ceil(num_inaccurate / vert_grounding_multipliers[num_inaccurate])  # n1 (также и n2)
    grounding_resistance = single_vertical_resistance / \
                           (num_accurate * vert_grounding_multipliers[num_inaccurate])  # Rcc

    # Определим сопротивление соединительной полосы Rп:

    horizontal_length = 1.05 * (num_accurate - 1) * eta * vertical_length  # lп
    horizontal_resistance = horizontal_value / (2 * math.pi * horizontal_length) * \
                            math.log(2 * horizontal_length ** 2 / (width * depth))  # Rп

    # Произведём уточнение
    if scheme == "в ряд":
        horiz_grounding_multipliers = {2: 0.94, 4: 0.89, 6: 0.84, 8: 0.8, 10: 0.75, 20: 0.56}  # таблица 5.4
    else:
        horiz_grounding_multipliers = {4: 0.70, 6: 0.64, 10: 0.56, 20: 0.45, 40: 0.39, 60: 0.36, 100: 0.33}

    horizontal_resistance = horizontal_resistance / horiz_grounding_multipliers[num_accurate]

    total_resistance = round(grounding_resistance * horizontal_resistance /
                             (grounding_resistance + horizontal_resistance), 2)

    return diameter, vertical_length, num_accurate, scheme, vertical_length * eta, round(width * 1000), \
        horizontal_length, depth, total_resistance, normative_resistance


if __name__ == '__main__':
    print(main(400, 'суглинок', '2', 'в ряд'))
