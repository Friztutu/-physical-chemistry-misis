import math


# 72.528 * math.pow(x, -0.982)
# 18.837 * math.pow(x, -0,952)

# Ввод: P (мощность) # Соединение обмоток Y/Y # l, метры # Uф 220 вольт # медь/алюминий # D, метры # тип AB или П# номинальный ток

def calculate(power, connection, length, voltage, metal, slice, distance, type, current):
    impedance_table_1 = {25: 3.110, 40: 1.950, 63: 1.240, 100: 0.800, 160: 0.487,
                         250: 0.312, 400: 0.195, 630: 0.129, 1000: 0.081, 1600: 0.054}
    impedance_table_2 = {25: 0.906, 40: 0.562, 63: 0.360, 100: 0.266, 160: 0.141,
                         250: 0.090, 400: 0.056, 630: 0.042, 1000: 0.029, 1600: 0.017}

    if power not in impedance_table_1 and connection:
        impedance = 72.528 * math.pow(power, -0.982)
    elif power not in impedance_table_2:
        impedance = 18.837 * math.pow(power, -0.952)
    elif connection:
        impedance = impedance_table_1[power]
    else:
        impedance = impedance_table_2[power]

    if current < 100:
        k = 1.4
    else:
        k = 1.25

    short_current = k * current

    square_table = [80, 120, 150, 160, 200, 250, 300]
    square_table_index = 6
    null_current = short_current / square_table[square_table_index]

    while null_current <= 0.5 or null_current >= 2:
        try:
            square_table_index -= 1
            null_current = short_current / square_table[square_table_index]
        except IndexError:
            return "Данных для расчёта нет в таблице, приносим свои извинения"

    res_table_05 = {80: (5.24, 3.14), 120: (3.66, 2.2), 150: (3.38, 2.03), 160: (2.8, 1.68),
                    200: (2.28, 1.37), 250: (2.1, 1.26), 300: (1.77, 1.06)}

    res_table_1 = {80: (4.2, 2.52), 120: (2.91, 1.75), 150: (2.56, 1.54), 160: (2.24, 1.34),
                   200: (1.79, 1.07), 250: (1.60, 0.96), 300: (1.34, 0.8)}

    res_table_15 = {80: (3.48, 2.09), 120: (2.38, 1.43), 150: (2.08, 1.25), 160: (1.81, 1.09),
                    200: (1.45, 0.87), 250: (1.28, 0.77), 300: (1.08, 0.65)}

    res_table_2 = {80: (2.97, 1.78), 120: (2.04, 1.22), 150: (1.6, 0.98), 160: (1.54, 0.92), 200: (1.24, 0.74)}

    if 0.5 <= null_current < 1:
        r1 = res_table_05[square_table[square_table_index]][0]
        x1 = res_table_05[square_table[square_table_index]][1]
        span = 1
    elif 1 <= null_current < 1.5:
        r1 = res_table_1[square_table[square_table_index]][0]
        x1 = res_table_1[square_table[square_table_index]][1]
        span = 2
    elif 1.5 <= null_current < 2:
        r1 = res_table_15[square_table[square_table_index]][0]
        x1 = res_table_15[square_table[square_table_index]][1]
        span = 3
    else:
        r1 = res_table_2[square_table[square_table_index]][0]
        x1 = res_table_2[square_table[square_table_index]][1]
        span = 4

    check_dictionary = {1: res_table_05, 2: res_table_1, 3: res_table_15, 4: res_table_2}

    null_active_resistance = r1 * length
    null_reactive_resistance = x1 * length

    if metal:
        resistivity = 0.018
    else:
        resistivity = 0.028

    phase_impedance = resistivity * length / slice
    null_impedance = math.sqrt(math.pow(null_active_resistance, 2) + math.pow(null_reactive_resistance, 2))
    diameter = 2 * math.sqrt(slice/math.pi)
    loop_reactive_resistance = 0.1256 * length * math.log1p(2 * distance / diameter)

    complete_impedance = math.sqrt(math.pow(null_active_resistance + phase_impedance, 2)
                                   + math.pow(null_reactive_resistance + loop_reactive_resistance, 2))

    calculated_current = voltage / (impedance/3 + complete_impedance)

    return calculated_current


