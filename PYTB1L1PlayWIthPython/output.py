Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print naam('mijn naam is raf')
SyntaxError: invalid syntax
>>> print('mijn naam is raf')
mijn naam is raf
>>> naam = "raf"
>>> naam
'raf'
>>> print(naam.upper())
RAF
>>> print(nam[0:2])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(nam[0:2])
NameError: name 'nam' is not defined
>>> print(naam[0:2])
ra
>>> print(naam[::-1])
far
>>> 
>>> leeftijd = 16
>>> print("hallo " + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
hallo raf ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
SyntaxError: invalid syntax
>>> output.py
SyntaxError: invalid syntax
>>> >>> from random import randint
>>> randint(0,1000)
573
>>> willekeurig_getal = randint(0,1000)
>>>
>>> willekeurig_getal
843
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 843
>>> from datetime import datetime
>>>
>>> datum = datetime.now()
>>>
>>> print(datum)
2020-09-23 11:29:18.401634
>>> datum.strftime('%A %d %B %Y')
'Wednesday 23 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'woensdag 23 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>>
>>> datum.strftime('%A %d %B %Y')
'mercoledì 23 settembre 2020'
>>>
