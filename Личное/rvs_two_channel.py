


from random import *
from math import *

def Tz2(lambd, t_):
    p = random()
    t = []
    t.append(round((-1/lambd) * log(p), 4))
    j = 0
    while t[j] < t_:
        j += 1
        p = random()
        t.append(round(t[j-1] + ((-1/lambd) * log(p)), 4))

    return t

def model(mu, lambd, t_):
    t = Tz2(lambd, t_)  # Генерируем время прихода программ
    print(t)

    vremya_prixoda_zayavok = t
    otkaz = 0
    obrabotka = 0
    vremya_prostoya = [0, 0]  # Time prostoya
    current_time = [vremya_prixoda_zayavok[0], vremya_prixoda_zayavok[0]]  # Время прихода для каждого канала
    vremya_zayavki = [(-1/mu) * log(random()) for _ in range(2)]  # Время обслуживания для каждого канала
    vremya_konca_zayavki = [current_time[i] + vremya_zayavki[i] for i in range(2)]

    i = 0
    while vremya_prixoda_zayavok[i] < t_:
        if vremya_konca_zayavki[0] > vremya_prixoda_zayavok[i] > vremya_konca_zayavki[1]:
            min_channel = vremya_konca_zayavki.index(min(vremya_konca_zayavki))
            vremya_prostoya[min_channel] += (vremya_prixoda_zayavok[i] - vremya_konca_zayavki[min_channel])
            current_time[min_channel] = vremya_prixoda_zayavok[i]
            vremya_zayavki[min_channel] = (-1/mu) * log(random())
            vremya_konca_zayavki[min_channel] = current_time[min_channel] + vremya_zayavki[min_channel]
            obrabotka += 1
        else:
            otkaz += 1
        i += 1

    model = {
        'otkaz': otkaz,
        'obrabotka': obrabotka,
        'vsego': i,
        'veroyatnost_obrabotki': round((i - otkaz) / i, 4),
        'vremya_prostoya': [round(v, 4) for v in vremya_prostoya],
        'vremya_posledney_zayavki': vremya_prixoda_zayavok[i - 1],
        'veroyatnost_prostoya': [round(v / vremya_prixoda_zayavok[i], 4) for v in vremya_prostoya]
    }

    return model

a = model(0.6, 0.5, 19)
print(a)
