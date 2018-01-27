#!/usr/bin/env python

from struct import (pack, calcsize)
from binascii import (unhexlify, hexlify)
from hashlib import sha256

class BitBlockHeaderHash(object):
    def __init__(self, version, previous_block_hash, merkle_root, time, bits,
                 nonce):
        self.version = version
        self.pbh = previous_block_hash
        self.merkle_root = merkle_root
        self.time = time
        self.bits = bits
        self.nonce = nonce


    '''
    version - Version
    '''
    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, v):
        if not isinstance(v, int):
            raise ValueError("Version must be an integer")
        if not (v > 0):
            raise ValueError("Version must be positive")
        self._version = v


    '''
    pbh - Previous Block Hash
    '''
    @property
    def pbh(self):
        return self._pbh

    @pbh.setter
    def pbh(self, previous_block_hash):
        try:
            int(previous_block_hash, 16)
        except ValueError:
            raise ValueError("Previous Block Hash must be a hexadecimal string")
        if not (len(unhexlify(previous_block_hash.encode("utf8"))) == 32):
            raise ValueError("Previous Block Hash must be 32 bytes hexadecimal")
        self._pbh = previous_block_hash


    '''
    merkle_root - Merkle Root
    '''
    @property
    def merkle_root(self):
        return self._merkle_root

    @merkle_root.setter
    def merkle_root(self, mr):
        try:
            int(mr, 16)
        except ValueError:
            raise ValueError("Merkle Root must be a hexadecimal string")
        if not (len(unhexlify(mr.encode("utf8"))) == 32):
            raise ValueError("Merkle Root must be 32 bytes hexadecimal")
        self._merkle_root = mr


    '''
    time - Unix Timestamp
    '''
    @property
    def time(self):
        return self._time

    # TODO - validate time in a better way
    @time.setter
    def time(self, timestamp):
        if not isinstance(timestamp, int) or not timestamp > 0:
            raise ValueError("Timestamp is bad")
        self._time = timestamp


    '''
    bits - nBits
    '''
    @property
    def bits(self):
        return self._bits

    @bits.setter
    def bits(self, b):
        if not isinstance(b, int):
            raise ValueError("Bits must be an integer")
        if not (b > 0):
            raise ValueError("Bits must be positive")
        self._bits = b


    '''
    nonce - Nonce
    '''
    @property
    def nonce(self):
        return self._nonce

    @nonce.setter
    def nonce(self, n):
        if not isinstance(n, int):
            raise ValueError("Nonce must be an integer")
        self._nonce = n


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

