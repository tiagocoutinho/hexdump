01 - dump binary data string
============================

Python 2

   >>> import hexdump
   >>> hexdump.hexdump('\x00'*16)
   0000000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................

Python 3

   >>> import hexdump
   >>> hexdump.hexdump('\x00'*16)
   0000000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................

   ^ this one is actually wrong, the data that is read from a
     binary file is `bytes`, not `string' as here, so there is
     information loss when such string is dumped

  [ ] investigate why no error is shown when writing UTF-8 text
      and data loss occurs
  [ ] provide an explanation why Python 3 strings can not be
      dumped (they are abstract unicode) and how to convert
      them to binary
