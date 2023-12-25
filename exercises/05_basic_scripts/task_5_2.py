# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

 #см. задание 4_8

"""
 A=int(ip.split('.')[0])
 B=int(ip.split('.')[1])
 C=int(ip.split('.')[2])
 D=int(ip.split('.')[3])
 print("{:<10}{:<10}{:<10}{:<10}".format(ip_1, ip_2, ip_3, ip_4))
 print("{:08b}  {:08b}  {:08b}  {:08b}".format(ip_1, ip_2, ip_3, ip_4))
"""
name = input('Введите параметры IP-сети в формате: 10.1.1.0/24 : ')

Network = name.split('.')

ip_1=int(Network[0])
ip_2=int(Network[1])
ip_3=int(Network[2])
ip_4=int(Network[-1].split('/')[0])
Mask=int(Network[-1].split('/')[1])

print('Network:')
print("{:<10}{:<10}{:<10}{:<10}".format(ip_1, ip_2, ip_3, ip_4))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(ip_1, ip_2, ip_3, ip_4))

print()

print('Mask:')
print('/'+str( Mask))
Mask_str_bin='1'*Mask + '0'*(32-Mask)
WildCard=Mask_str_bin[::-1]
Mask_str_bin_1=Mask_str_bin[0:8]
Mask_str_bin_2=Mask_str_bin[8:16]
Mask_str_bin_3=Mask_str_bin[16:24]
Mask_str_bin_4=Mask_str_bin[24:]

Mask_bin_1=int(Mask_str_bin_1,2) #воспринимаем строку как двоичное число и переводим в число(десятичное)
Mask_bin_2=int(Mask_str_bin_2,2)
Mask_bin_3=int(Mask_str_bin_3,2)
Mask_bin_4=int(Mask_str_bin_4,2)

print("{:<10}{:<10}{:<10}{:<10}".format(Mask_bin_1, Mask_bin_2, Mask_bin_3, Mask_bin_4))
print("{:<10}{:<10}{:<10}{:<10}".format(Mask_str_bin_1, Mask_str_bin_2, Mask_str_bin_3, Mask_str_bin_4))





