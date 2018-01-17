#!/usr/bin/python

from struct import pack
from binascii import (unhexlify, hexlify)
from hashlib import sha256

def hexToLE(hexa):
	'''
	Changes the byte order of a hexadecimal number to little-endian
	Can't use pack here due to the size of the number
	'''
	bin_of_hexa = unhexlify(hexa)
	return hexlify(bin_of_hexa[::-1])

def intToHexLE(n):
	'''
	Converts an integer to a 4 byte hexadecimal in little-endian byte order
	'''
	return hexlify(pack("<I", n))
	# check n.to_bytes(4, byteorder = 'little') for python > 3.2 
	

correct_header = "01000000bddd99ccfda39da1b108ce1a5d70038d0a967bacb68b6b63065f626a0000000044f672226090d85db9a9f2fbfe5f0f9609b387af7be5b7fbb7a1767c831c9e995dbe6649ffff001d05e0ed6d"

version = intToHexLE(1)
previousblockhash = hexToLE("000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd")
merkleroot = hexToLE("999e1c837c76a1b7fbb7e57baf87b309960f5ffefbf2a9b95dd890602272f644")
time = intToHexLE(1231470173)
bits = hexToLE("1d00ffff")
nonce = intToHexLE(1844305925)

header = version + "" + previousblockhash + "" + merkleroot + "" + time + "" + bits + "" + nonce

header_bin=unhexlify(header)

hash = sha256(sha256(unhexlify(header)).digest()).digest()
print hash[::-1].encode('hex_codec')

