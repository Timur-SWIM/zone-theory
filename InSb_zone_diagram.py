import matplotlib.pyplot as plt
import numpy as np
from numpy import log as ln 

aInSb = 5.1*1e-4 #Температурный коэффициент

Eg0InSb = 0.23  #Ширина запрещенной зоны при 0K, эВ

mz_eInSb = 0.013 #эффективная масса электрона для InSb
mz_pInSb = 0.6  #эффективная масса дырки для InSb

k=1.38*1e-23 #постоянная Больцмана

T1 = 52  # первая температура в Кельвинах
T2 = 300 # воторая температура в Кельвинах

#расчет запрещенной зоны при T1 и T2
Eg_InSb_T1 = Eg0InSb - aInSb * T1
Eg_InSb_T2 = Eg0InSb - aInSb * T2

#расчет положения уровня Ферми от температуры
Ef_InSb_T1 = (3/4*k*T1*ln(mz_eInSb/mz_pInSb))/(1.6*1e-19)
Ef_InSb_T2 = (3/4*k*T2*ln(mz_eInSb/mz_pInSb))/(1.6*1e-19)

#расчет валентной зоны
InSb_Ev = 0

#построение диаграммы для InSb
plt.figure(figsize=(8, 6))

#Валентная зон
plt.fill_between([0,1],-(Eg_InSb_T1/2 - Eg_InSb_T1/4), InSb_Ev,
                color='blue',
                alpha=0.3,
                label='Valence Band T1')

plt.fill_between([1.5, 2.5], -(Eg_InSb_T2/4), InSb_Ev,
                color='blue',
                alpha=0.3,
                label='Valence Band T2')

#Зона проводимости
plt.fill_between([0,1], Eg_InSb_T1, Eg_InSb_T1 + Eg_InSb_T1/4,
                 color='green',
                 alpha=0.3,
                 label='Conduction Band T1')

plt.fill_between([1.5, 2.5], Eg_InSb_T2, Eg_InSb_T2 + Eg_InSb_T2/4,
                 color='orange',
                 alpha=0.3,
                 label='Conduction Band T2')

#Середина запрещенной зоны
plt.hlines(Eg_InSb_T1/2, 0, 1, 
           color='black', 
           alpha=0.5,
           linestyle='-', 
           label=f'Forbidden zone T1 = {round(Eg_InSb_T1/2, 4)} / {round(Eg_InSb_T1/2, 4)} eV')

plt.hlines(Eg_InSb_T2/2, 1.5, 2.5, 
           color='black', 
           alpha=0.5,
           linestyle='-', 
           label=f'Forbidden zone T2 = {round(Eg_InSb_T2/2, 4)} eV')

#Уровень Ферми
plt.hlines(Eg_InSb_T1/2 + Ef_InSb_T1, 0, 1,
           color='red',
           linestyle='--',
           label=f'Fermi Leve T1 = {round(Ef_InSb_T1, 4)} eV')

plt.hlines(Eg_InSb_T2/2 + Ef_InSb_T2, 1.5, 2.5,
           color='red',
           linestyle='--',
           label=f'Fermi Level T2 = {round(Ef_InSb_T2, 4)} eV')

# Остальные настройки
plt.ylim(InSb_Ev - 0.5, 
         max(Eg_InSb_T1, Eg_InSb_T2) + 1.5)

plt.xticks([0.5, 2], ['T1', 'T2'])

plt.ylabel('Energy (eV)')

plt.title('Energy Band Diagram for InSb')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()