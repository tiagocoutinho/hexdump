01 - dump binary data string
============================

Python 2

   >>> import hexdump
   >>> hexdump.hexdump('\x00'*16)
   0000000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................

Python 3

   >>> import hexdump
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File ".\hexdump.py", line 76
       print line
                ^
   SyntaxError: invalid syntax
