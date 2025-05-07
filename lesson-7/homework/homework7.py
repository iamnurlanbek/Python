"""1. is_prime(n) funksiyasi
is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

Misollar:
Kiritish:
4
Natija:
False
(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

Kiritish:
7
Natija:
True
(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)"""


# def is_prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False           
# print(is_prime(7))

"""2. digit_sum(k) funksiyasi
digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

Misollar:
Kiritish:
24
Natija:
6
(Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

Kiritish:
502
Natija:
7
(Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)

"""

def digit_sum(k):
    summa = 0
    nums = list(str(k))
    
    for i in nums:
        summa += int(i)       
    return summa
print(digit_sum(244))

"""3. Ikki sonning darajalari
Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.

Misol:
Kiritish:
10
Natija:
2 4 8
(Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)"""


# option 1
def ndaraja(N):
    daraja = 1
    while daraja < N:
        if 2 ** daraja <= N:
            print(2 ** daraja)
            daraja += 1
        else:
            break
ndaraja(10)


# option 2
def ndaraja(N):
    a = 2
    while a <= N:
        print(a)
        a *= 2
ndaraja(10)
