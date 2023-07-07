"""
Расчет зануления

Цель расчета зануления – определить сечение защитного нулевого провода,
удовлетворяющее условию срабатывания максимальной токовой защиты, при известных
остальных параметрах сети и заданных параметрах автоматического выключателя или
плавкой вставки.

Подобрать площадь сечения нулевого провода, удовлетворяющая условию
срабатывания максимальной токовой защиты, распределительного щитка лаборатории, к
которому подведена линия (длиной l = 200 м) от понижающего трансформатора с 10 кВ до
0,4 кВ, мощностью 400 кВ·А, соединение обмоток Y/Yн. Параметры «фазы» -- напряжение
220 В, площадь сечения провода из меди 10 мм2. Расстояние между проводниками линии –
0,6 м. Параметры устройства защиты – тип АВ, номинальный ток Iном = 63 А.
"""

import math


# Определим сопротивление обмоток трансформатора Zт, Ом
def init_varibles(scheme_id, power_key, phase_voltage_db, length_db, phase_square_db, phase_material_id,
                  distance_between_conductors_db, amperage_nominal_db):
    scheme_dict = {1: 'звезда-звезда', 2: 'не звезда-звезда'}
    material_dict = {1: 'алюминий', 2: 'медь'}
    powers = {1: 40, 2: 63, 3: 400, 4: 630}

    scheme = scheme_dict[scheme_id]
    power = powers[power_key]
    phase_voltage = phase_voltage_db
    length = length_db
    phase_square = phase_square_db
    phase_material = material_dict[phase_material_id]
    distance_btwn_conductors = distance_between_conductors_db
    amperage_nominal = amperage_nominal_db
    return calculate(scheme, power, phase_voltage, length, phase_square, phase_material, distance_btwn_conductors, amperage_nominal)


def calculate(scheme, power, phase_voltage, length, phase_square, phase_material, distance_btwn_conductors, amperage_nominal):
    if scheme == "звезда-звезда":
        resistance_table = {25: 3.110, 40: 1.950, 63: 1.240, 100: 0.800, 160: 0.487,
                            250: 0.312, 400: 0.195, 630: 0.129, 1000: 0.081, 1600: 0.054}  # Таблица 5.6
    else:
        resistance_table = {25: 0.906, 40: 0.562, 63: 0.360, 100: 0.266, 160: 0.141,
                            250: 0.090, 400: 0.056, 630: 0.042, 1000: 0.029, 1600: 0.017}

    transformer_resistance = resistance_table[power] / 3 if 126 <= phase_voltage <= 130 else resistance_table[
        power]  # Zт

    coef = 1.4 if amperage_nominal < 100 else 1.25  # k
    amperage_short = amperage_nominal * coef  # Iк

    # Рассчитаем плотность тока в нулевом проводнике
    # Найдем максимально и минимально возможные значения площади поперечного сечения
    square_max = amperage_short / 0.5
    square_min = amperage_short / 2

    conductor_resistances = {80: {0.5: (5.24, 3.14), 1.0: (4.20, 2.52), 1.5: (3.48, 2.09), 2.0: (2.97, 1.78)},
                             120: {0.5: (3.66, 2.20), 1.0: (2.91, 1.75), 1.5: (2.38, 1.43), 2.0: (2.04, 1.22)},
                             150: {0.5: (3.38, 2.03), 1.0: (2.56, 1.54), 1.5: (2.08, 1.25), 2.0: (1.60, 0.98)},
                             160: {0.5: (2.80, 1.68), 1.0: (2.24, 1.34), 1.5: (1.81, 1.09), 2.0: (1.54, 0.92)},
                             200: {0.5: (2.28, 1.37), 1.0: (1.79, 1.07), 1.5: (1.45, 0.87), 2.0: (1.24, 0.74)},
                             250: {0.5: (2.10, 1.26), 1.0: (1.60, 0.96), 1.5: (1.28, 0.77)},
                             300: {0.5: (1.77, 1.06), 1.0: (1.34, 0.80), 1.5: (1.08, 0.65)}}  # Таблица 5.7

    # Выберем площадь, входящую в найденный диапозон
    for square in filter(lambda current_square: square_min <= current_square <= square_max, conductor_resistances):
        # Выберем подходящую плотность тока
        for amper_density in conductor_resistances[square]:  # iн
            active_table_resistance = conductor_resistances[square][amper_density][0]  # r1
            inductive_table_resistance = conductor_resistances[square][amper_density][1]  # x1

            #   Определим значения активного и индуктивного сопротивления нулевого защитного
            #   проводника
            null_active_resistance = active_table_resistance * length / 1000  # Rн
            null_inductive_resistance = inductive_table_resistance * length / 1000  # Xн

            #   Для медных и алюминиевых проводников фаз по известным данным: сечению Sф (мм2),
            #   длине l (м) и удельному сопротивлению проводника (Ом·мм2/м) (для меди = 0,018, а для
            #   алюминия = 0,028) – опредеим активное сопротивление фазы Rф
            resistivity = 0.018 if phase_material == "медь" else 0.028  # p

            phase_active_resistance = resistivity * length / phase_square  # Rф

            #   Значение внутреннего индуктивного фазного сопротивления Xф для медных и
            #   алюминиевых проводников пренебрежимо мало

            #   По формуле полного сопротивления проводников определим полное сопротивление
            #   фазного Zф (Ом) и нулевого защитного проводника Zн (Ом)
            total_null_resistance = (null_active_resistance ** 2 + null_inductive_resistance ** 2) ** 0.5  # Zн
            total_phase_resistance = phase_active_resistance  # Zф

            #   Тут должна быть проверка Zн <= 2 * Zф

            #   Определим внешнее индуктивное сопротивление Xп, Ом, петли «фаза-нуль»
            diameter = 2 * math.sqrt(phase_square / math.pi) / 10 ** 6
            outer_inductive_resistance = 0.1256 * length / 1000 * \
                                         math.log(2 * distance_btwn_conductors / diameter)  # Xп

            #   Полное сопротивление проводников петли «фаза-нуль» Zп (Ом)
            phase_null_resistance = math.sqrt((phase_active_resistance + null_active_resistance) ** 2 +
                                              (0 + null_inductive_resistance + outer_inductive_resistance) ** 2)  # Zп

            #   Расчетный ток петли «фаза-нуль»
            phase_null_amperage = phase_voltage / (transformer_resistance / 3 + phase_null_resistance)

            #   Проверка условия на срабатывание выключателя
            if phase_null_amperage >= amperage_short:
                return square

    return -100
