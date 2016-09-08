# -*- coding: utf-8 -*-

# das obige Kommentar ermöglicht es, in Python 2 Umlaute zu schreiben
# (dazu wird die Zeichencodierung der Datei definiert)

# durch __future__ in Python 2 möglich:
from __future__ import unicode_literals
# ermöglicht zB den string "⠎😀⠎ß" im Programm zu schreiben

from __future__ import print_function
# print 'abc' -> print('abc')

from __future__ import division
# 3/2 = 1.5


b = "Grüß Gott"
print(b)


# nur in Python 3:
# raw_input() -> input()

3 > 'abc'
# Python 2 lässt int und str vergleichen, Python 3 gibt Fehler aus

print(range(3))
# Python 2: [0, 1, 2] -> das ist eine Echte Liste
# Python 3: range(0, 10) -> das ist keine echte Liste (spart Speicherplatz)
