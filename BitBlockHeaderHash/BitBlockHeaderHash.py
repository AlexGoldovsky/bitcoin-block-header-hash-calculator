#!/usr/bin/env python

from struct import pack
from binascii import (unhexlify, hexlify)
from hashlib import sha256

class BitBlockHeaderHash:
    def __init__(self, version, previous_block_hash, merkle_root, time, bits,
                 nonce):
        self.version = version
        self.pbh = previous_block_hash
        self.merkle_root = merkle_root
        self.time = time
        self.bits = bits
        self.nonce = nonce

    def __hexToLE(self, hexa):
        '''
        Changes the byte order of a hexadecimal number to little-endian
        Can't use pack here due to the size of the number
        '''
        bin_of_hexa = unhexlify(hexa)
        return hexlify(bin_of_hexa[::-1])

    def __intToHexLE(self, n):
        '''
        Converts an integer to a 4 byte hexadecimal in little-endian byte order
        '''
        return hexlify(pack("<I", n))
        # check n.to_bytes(4, byteorder = 'little') for python > 3.2

    def get_header_hex(self):
        version = self.__intToHexLE(self.version)
        previousblockhash = self.__hexToLE(self.pbh)
        merkleroot = self.__hexToLE(self.merkle_root)
        time = self.__intToHexLE(self.time)
        bits = self.__intToHexLE(self.bits)
        nonce = self.__intToHexLE(self.nonce)

        return "".join([version, previousblockhash, merkleroot, time, bits,
                       nonce])

    def calculate_hash(self):
        header_hex = self.get_header_hex()
        header_bin = unhexlify(header_hex)
        header_hash = sha256(sha256(header_bin).digest()).digest()
        return header_hash[::-1].encode('hex_codec')

