# Zavala Medina Alexia Paola | NC = 0150

import matplotlib.pyplot as plt

materias = ["Mate", "Ciencias", "Filosofia", "Vision", "Machine"]

calificaciones = [90, 85, 78, 95, 88]

plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')

plt.title("Calificaciones - NC: 0150")
plt.xlabel("Materias evaluadas")
plt.ylabel("Porcentaje")

plt.show()

print("Zavala Medina Alexia Paola | NC = 0150")