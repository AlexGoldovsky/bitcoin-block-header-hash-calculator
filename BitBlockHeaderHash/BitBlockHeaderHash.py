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

    def __hexToLEBin(self, hexstr):
        '''
        Converts a hexadecimal string to a binary little-endian byte order
        '''
        return unhexlify(hexstr)[::-1]

    def __intToLEBin(self, n):
        '''
        Converts an integer to a binary little-endian byte order
        '''
        return pack("<I", n)

    def get_header_hex(self):
        version = self.__intToLEBin(self.version)
        previousblockhash = self.__hexToLEBin(self.pbh)
        merkleroot = self.__hexToLEBin(self.merkle_root)
        time = self.__intToLEBin(self.time)
        bits = self.__intToLEBin(self.bits)
        nonce = self.__intToLEBin(self.nonce)

        return "".join([version, previousblockhash, merkleroot, time, bits,
                       nonce])

    def calculate_hash(self):
        header_bin = self.get_header_hex()
        header_hash = sha256(sha256(header_bin).digest()).digest()
        return header_hash[::-1].encode('hex_codec')

