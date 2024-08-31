# locale para internacionalização
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/internation
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(locale.getlocale())

print(calendar.calendar(2022))