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


02 - restore binary data from hex dump string
==============================================

Python 2

   >>> import hexdump
   >>> res = hexdump.restore(
   ... '0000000010: 00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF  .."3DUfw........')
   >>> res
   '\x00\x11"3DUfw\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
   >>> type(res)
   <type 'str'>

Python 3

   >>> import hexdump
   >>> res = hexdump.restore(
   ... '0000000010: 00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF  .."3DUfw........')
   >>> res
   b'\x00\x11"3DUfw\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
   >>> type(res)
   <class 'bytes'>

