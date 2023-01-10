import locale

locale.setlocale(locale.LC_ALL, '')
'ru_RU.UTF-8'
print(locale.format_string('%d', 1258111, grouping=True))


