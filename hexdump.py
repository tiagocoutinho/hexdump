# -*- coding: latin-1 -*-
#!/usr/bin/env python
#
# Dump binary data into the text format:
#
# 0000000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
# 
#
# It is similar to the one used by:
# Scapy
# 00 00 00 5B 68 65 78 64 75 6D 70 5D 00 00 00 00  ...[hexdump]....
# 00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF  .."3DUfw........
#
# Far Manager
# 000000000: 00 00 00 5B 68 65 78 64 ¦ 75 6D 70 5D 00 00 00 00     [hexdump]
# 000000010: 00 11 22 33 44 55 66 77 ¦ 88 99 AA BB CC DD EE FF   ?"3DUfwˆ™ª»ÌÝîÿ

__version__ = '0.0dev'
__author__  = 'anatoly techtonik <techtonik@gmail.com>'
__license__ = 'Public Domain'

import sys

# --- constants
PY3K = sys.version_info >= (3, 0)

# --- helpers
def int2byte(i):
  '''convert int [0..255] to binary byte'''
  if PY3K:
    return i.to_bytes(1, 'little')
  else:
    return chr(i)

def chunks(seq, size): 
  '''Cut sequence into chunks of given size. If `seq` length is 
     not divisible by `size` without reminder, last chunk will 
     have length less than size. 

     >>> list( chunks([1,2,3,4,5,6,7], 3) ) 
     [[1, 2, 3], [4, 5, 6], [7]] 
  ''' 
  endlen = len(seq)//size 
  for i in range(endlen): 
    yield [seq[i*size+n] for n in range(size)] 
  if len(seq) % size: 
    yield seq[endlen*size:] 

# --- stuff
def hexdump(data):
  # the format is (80 symbols wide)
  # 0000000000:  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
  output = ''
  for d in chunks(data, 16):
    for byte in d[:8]:
      print "%02X" % ord(byte),
    print '',
    for byte in d[8:]:
      print "%02X" % ord(byte),
    print ''

hexdump('z'*20)
