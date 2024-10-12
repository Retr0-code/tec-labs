import math as m

R = 100
L = 6.8 * 10**(-3)
C = 68 * 10**(-9)

def Amperage (Us : dict) -> dict:
    global R
    Is = {}

    for angle, U in Us.items():
        Is[angle] = round(Us[angle] / R * 10**3, 4)

    return Is

#1st point
#1.3
U_RLout = {
    5:  0.9,
    10: 0.88,
    20: 0.82,
    30: 0.78,
    40: 0.77,
    50: 0.56,
    60: 0.42,
    70: 0.28,
    80: 0.17
}
I_L_mA = Amperage(U_RLout)
print("1.3 I_mA: ", I_L_mA)

#2.3
U_RCout = {
    -5:  1,
    -10: 0.84,
    -20: 0.82,
    -30: 0.76,
    -40: 0.68,
    -50: 0.56,
    -60: 0.4,
    -70: 0.26,
    -80: 0.16
}
I_C_mA = Amperage(U_RCout)
print("2.3 I_mA: ", I_C_mA)

#3.3
U_RLCout = {
    -80: 0.12,
    -70: 0.23,
    -60: 0.34,
    -50: 0.45,
    -40: 0.56,
    -30: 0.63,
    -20: 0.65,
    -10: 0.68,
    -5: 0.69,
    0: 0.7,
    5: 0.69,
    10: 0.68,
    20: 0.65,
    30: 0.6,
    40: 0.53,
    50: 0.44,
    60: 0.35,
    70: 0.26,
    80: 0.16
}
I_RLC_mA = Amperage(U_RLCout)
print("3.3 I_mA: ", I_RLC_mA, "\n")

#2nd point
#2.1
print("RL:")
phi_1 = 50
U_c = U_RLout[phi_1]
R_l = round(R * (1 / U_c) * m.cos(m.radians(phi_1)) - R, 3)
X_l = round(R * (1 / U_c) * m.sin(m.radians(phi_1)) - R, 3)
print(f"R_l: Z*_out = {R_l} + j * {X_l}")
print(f"R_l = {R_l}, X_l = {X_l}\n")

print("RC:")
phi_2 = -50
U_c = U_RCout[phi_2]
R_in = round(R * (1 / U_c) * m.cos(m.radians(phi_2)) - R, 3)
X_c = round(R * (1 / U_c) * m.sin(m.radians(phi_2)) - R, 3)
G_c = round(1 / R_in, 3)
print(f"G_c: Z*_out = {R_in} + j * {X_c}")
print(f"G_c = 1 / R_in => G_c = {G_c} X_c = {X_c}")

#2.2
print(f"Добротность катушки Q_L = X_l / R_l => Q_L = {round(X_l / R_l, 2)}")
print(f"Добротность конденсатора Q_c = X_c * G_c => Q_c = {round(X_c * G_c, 2)}\n")

#3rd point
#3.1

# RL
freq = 2.9 * 10**3
w = freq * m.pi * 2
print("RL цепь")
print(f"R_10 = {R} Om, пусть L = L_1 = {L} Гн")
print("ФЧХ = fi(w) = arctg(wL/R) => fi(w) =",  m.atan((m.radians(w * L / R))))
print("АЧХ = K(w) = R * sqr(1 + (wL/R)**2) => K(w) =", R * m.sqrt(1 + (w * L / R)**2))

# RC
freq = 18.2 * 10**3
w = freq * m.pi * 2
print("RC цепь")
print(f"R_10 = {R} Om, пусть C = C_1 = {C} F")
print("ФЧХ = fi(w) = -arctg(wRC) => fi(w) =", (- m.atan(m.radians(w * R * C))))
print("АЧХ = K(w) = 1 / sqr(1 + (wRC)**2) => K(w) =", 1 / m.sqrt(1 + (w * R * C)**2))

# 4
I_m40 = 0.0056 / 10**3
U_out_m40 = 0.56
I_p40 = 0.0053 / 10**3
U_out_p40 = 0.53
freq_m40 = 6.2 * 10**3
freq_p40 = 6.2 * 10**3
print("АЧХ = K(w) = 1 / sqr( 1 + (wRC)**2) => K(w) =", 1 / m.sqrt(1 + (w * R * C)**2))
