#!/usr/bin/env python

from struct import pack
from binascii import unhexlify
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
            pbh_type = type(previous_block_hash).__name__
            raise ValueError("Previous Block Hash must be 32 bytes hexadecimal." +
                             "Got Type: %s Instead" %pbh_type)
        try:
            bytes_count = len(unhexlify(previous_block_hash.encode("utf8")))
            if not (bytes_count == 32):
                raise ValueError("Wrong Bytes Count: %d" %bytes_count)
        except (TypeError, ValueError) as e:
            raise ValueError("Previous Block Hash must be 32 bytes hexadecimal." +
                             "Got Error: %s Instead" %str(e))

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
            mr_type = type(mr).__name__
            raise ValueError("Merkle Root must be 32 bytes hexadecimal." +
                             "Got Type: %s Instead" %mr_type)
        try:
            bytes_count = len(unhexlify(mr.encode("utf8")))
            if not (bytes_count == 32):
                raise ValueError("Wrong Bytes Count: %d" %bytes_count)
        except (TypeError, ValueError) as e:
            raise ValueError("Merkle Root must be 32 bytes hexadecimal." +
                             "Got Error: %s Instead" %str(e))
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
        if not (n > -1):
            raise ValueError("Nonce must be positive or 0")
        self._nonce = n

    def __hex_to_le_bin(self, hexstr):
        """
        Converts a hexadecimal string to a binary little-endian byte order
        """
        return unhexlify(hexstr)[::-1]

    def __int_to_le_bin(self, n):
        """
        Converts an integer to a binary little-endian byte order
        """
        return pack("<I", n)

    def get_header_hex(self):
        version = self.__int_to_le_bin(self.version)
        previousblockhash = self.__hex_to_le_bin(self.pbh)
        merkleroot = self.__hex_to_le_bin(self.merkle_root)
        time = self.__int_to_le_bin(self.time)
        bits = self.__int_to_le_bin(self.bits)
        nonce = self.__int_to_le_bin(self.nonce)

        return "".join([version, previousblockhash, merkleroot, time, bits,
                       nonce])

    def calculate_hash(self):
        header_bin = self.get_header_hex()
        header_hash = sha256(sha256(header_bin).digest()).digest()
        return header_hash[::-1].encode('hex_codec')

