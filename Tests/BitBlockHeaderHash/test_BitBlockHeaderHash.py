import pytest
from BitBlockHeaderHash import BitBlockHeaderHash


class TestBitBlockHeaderHash(object):
    VERSION = 3
    PREV_BLOCK = "0000000000000000070aa22c35a04fcea22eea3319ffb618ed0e187db6d5e427"
    MERKLE_ROOT = "52e2ab6acfb694d49e71899cc2692c1713b9978a74a1662a847954c0a54da6a2"
    TIMESTAMP = 1442663665
    BITS = 403867578
    NONCE = 1290016663
    BLOCK_HASH = "0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6"

    def test_positive_flow(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() == self.BLOCK_HASH

    ###### START TEST VERSION #####
    def test_wrong_version(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION+1,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_negative_version_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=-1,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_char_version_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version="1",
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_missing_version_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)


    ##### END TEST VERSION #####


    ##### START PREVIOUS BLOCKHASH TEST #####
    def test_wrong_previous_block_hash(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash="1" + self.PREV_BLOCK[1:],
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_non_hexadecimal_previous_block_hash_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash="g" + self.PREV_BLOCK[1:],
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_non_32_odd_bytes_count_previous_block_hash_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK[1:],
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_non_32_even_bytes_count_previous_block_hash_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK[2:],
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_missing_previous_block_hash_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(version=self.VERSION,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    ##### END PREVIOUS BLOCKHASH TEST #####

    ##### START PREVIOUS BLOCKHASH TEST #####
    def test_wrong_merkle_root(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root="1" + self.MERKLE_ROOT[1:],
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_non_hexadecimal_merkle_root_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root="g" + self.MERKLE_ROOT[1:],
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_non_32_odd_bytes_count_merkle_root_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT[1:],
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_non_32_even_bytes_count_merkle_root_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT[2:],
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_missing_merkle_root_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=self.NONCE)

    ##### END PREVIOUS BLOCKHASH TEST #####


    ###### START TEST TIMESTAMP #####
    def test_wrong_time(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP+1,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_negative_time_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=-1,
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_char_time_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time="11111111",
                               bits=self.BITS,
                               nonce=self.NONCE)

    def test_missing_time_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               version=self.VERSION,
                               bits=self.BITS,
                               nonce=self.NONCE)


    ##### END TEST TIMESTAMP #####


    ###### START TEST BITS #####
    def test_wrong_bits(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS+1,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_negative_bits_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=-1,
                               nonce=self.NONCE)

    def test_char_bits_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits="11111111",
                               nonce=self.NONCE)

    def test_missing_bits_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               version=self.VERSION,
                               time=self.TIMESTAMP,
                               nonce=self.NONCE)


    ##### END TEST BITS #####


    ###### START TEST NONCE #####
    def test_wrong_nonce(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE+1)

        assert bbhh.calculate_hash() != self.BLOCK_HASH

    def test_negative_nonce_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce=-1)

    def test_char_nonce_rises_ValueError(self):
        with pytest.raises(ValueError):
            BitBlockHeaderHash(version=self.VERSION,
                               previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               time=self.TIMESTAMP,
                               bits=self.BITS,
                               nonce="11111111")

    def test_missing_nonce_rises_TypeError(self):
        with pytest.raises(TypeError):
            BitBlockHeaderHash(previous_block_hash=self.PREV_BLOCK,
                               merkle_root=self.MERKLE_ROOT,
                               version=self.VERSION,
                               time=self.TIMESTAMP,
                               bits=self.BITS)

    ##### END TEST BITS #####

