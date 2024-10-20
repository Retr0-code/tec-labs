import matplotlib.pyplot as plt
from matplotlib import gridspec

Is_mA = [41, -13, -1, -1, 42, 12]
Rs = [128, 228, 290, 300, 150, 475]
E1 = 11
E2 = 9

# Контур abcdefa
phi_a = 11
phi_b = phi_a - Is_mA[0] * Rs[0] / 10**3
phi_c = phi_b - Is_mA[3] * Rs[3] / 10**3
phi_d = phi_c - Is_mA[1] * Rs[1] / 10**3
phi_e = phi_d - E2
phi_f = phi_e - Is_mA[2] * Rs[2] / 10**3
phi_a_calc = phi_f + E1

phi_abcdefa = [phi_a, phi_b, phi_c, phi_d, phi_e, phi_f, phi_a_calc]

print(f'Проверка для контура abcdefa => {phi_a} ~ {phi_a_calc}')

# Контур bcefb
phi_b = 6.3
phi_c = phi_b - Is_mA[3] * Rs[3] / 10**3
phi_e = phi_c + Is_mA[5] * Rs[5] / 10**3
phi_f = phi_e - Is_mA[2] * Rs[2] / 10**3
phi_b_calc = phi_f - Is_mA[4] * Rs[4] / 10**3

phi_bcefb = [phi_b, phi_c, phi_e, phi_f, phi_b_calc]

print(f'Проверка для контура bcefb => {phi_b} ~ {phi_b_calc}')

figure = plt.figure(figsize=(16, 8))
gs = gridspec.GridSpec(1, 2, figure=figure)

def add_plot(axes, title, phi_array, R_array):
    axes.plot(R_array, phi_array)
    axes.set_xlabel('R, Ом')
    axes.set_ylabel('Phi, Кл')
    axes.grid()
    axes.set_title(title)

# График для abcdefa
axes_abcdefa = plt.subplot(gs[0])

R_c = [0, Rs[0]]
R_c.append(R_c[1] + Rs[3])
R_c.append(R_c[2] + Rs[1])
R_c.append(R_c[3])
R_c.append(R_c[4] + Rs[2])
R_c.append(R_c[5])

add_plot(axes_abcdefa, 'Потенциальная диаграмма контура abcdefa', phi_abcdefa, R_c)

# График для bcefb
axes_bcefb = plt.subplot(gs[1])

R_c = [0, Rs[3]]
R_c.append(R_c[1] + Rs[5])
R_c.append(R_c[2] + Rs[2])
R_c.append(R_c[3] + Rs[4])

add_plot(axes_bcefb, 'Потенциальная диаграмма контура bcefb', phi_bcefb, R_c)

plt.show()
