per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = []
for i in per_cent.values():
    x = i * money // 100
    deposit.append(int(x))
print('deposit =', deposit)
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать - ' + str(deposit_max))
deposit.clear()