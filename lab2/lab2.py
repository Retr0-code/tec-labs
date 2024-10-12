def Amperage (U_mas):
	I_mas = []
	for i in range(len(U_mas)):
		I_mas.append(round(U_mas[i]/100, 4))
	return I_mas

#1st point
#1.3
U_out = [0.9, 0.88, 0.82, 0.78, 0.77, 0.56, 0.42, 0.28, 0.17]
I_mA = Amperage(U_out)
print("1.3 I_mA: ", I_mA)

#2.3
U_out = [1, 0.84, 0.82, 0.76, 0.68, 0.56, 0.4, 0.26, 0.16]
I_mA = Amperage(U_out)
print("2.3 I_mA: ", I_mA)

#3.3
U_out = [0.12, 0.23, 0.34, 0.45, 0.56, 0.63, 0.65, 0.68, 0.69, 0.7, 0.69, 0.68, 0.65, 0.6, 0.53, 0.44, 0.35, 0.26, 0.16]
I_mA = Amperage(U_out)
print("3.3 I_mA: ", I_mA, "\n\n")

#2nd point
#2.1
import math as m

print("R_l: Z*_out =", round(100*(1/0.56)*m.cos(m.radians(50))-100, 3), "+ j", round(100*(1/0.56)*m.sin(m.radians(50)), 3))
print("R_l = 14.78, X_l = 136.8")

print("G_c: Z*_out =", round(100*(1/0.56)*m.cos(m.radians(-50))-100, 3), "+ j", round(100*(1/0.56)*m.sin(m.radians(-50)), 3))
print("G_c = 1/R_in => G_c =", round(1/14.78, 2), "X_c = 136.8")
#2.2

print("Добротность катушки Q_l = X_l/R_l => Q_l =", round(136.8/14.78,2))
print("Добротность конденсатора Q_c = X_c*R_c => Q_c =", round(136.8*0.007,2), "\n\n")

#3rd point
#3.1

R = 100
C = 47 * 10**(-9)
w = -50
print("RC цепь")
print("R_10 = 100 Om, пусть C = C_1 = 47 nF")
print("ФЧХ = fi(w) = -arctg(wRC) => fi(w) =", ( -1 * m.atan( m.radians(w * R * C))))
print("АЧХ = K(w) = 1 / sqr( 1 + (wRC)**2) => K(w) =", 1/m.sqrt(1 + (w*R*C)**2))

R = 100
L = 10 * 10**(-3)
w = 50
print("RL цепь")
print("R_10 = 100 Om, пусть L = L_1 = 10 мГн")
print("ФЧХ = fi(w) = arctg(wL/R) => fi(w) =",  m.atan( (m.radians(w*L/R)) ))
print("АЧХ = K(w) = R * sqr( 1 + (wL/R)**2) => K(w) =", R * m.sqrt(1 + (w*L/R)**2))
