s = "Invert me please"
s_mod = s[::-1]
print(s_mod)
# Спиздил и нихуя не понял
i = len(s) - 1
while i >= 0 :
    print(s[i])
    i = i - 1
# Тоже спиздил но не понял почему просто без join не работает
print(''.join(reversed(s)))