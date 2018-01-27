import pytest
from BitBlockHeaderHash import BitBlockHeaderHash


class TestBitBlockHeaderHash(object):
    VERSION=3
    PREV_BLOCK="0000000000000000070aa22c35a04fcea22eea3319ffb618ed0e187db6d5e427"
    MERKLE_ROOT="52e2ab6acfb694d49e71899cc2692c1713b9978a74a1662a847954c0a54da6a2"
    TIMESTAMP=1442663665
    BITS=403867578
    NONCE=1290016663
    BLOCK_HASH="0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6"

    def test_positive_flow(self):
        bbhh = BitBlockHeaderHash(version=self.VERSION,
                                  previous_block_hash=self.PREV_BLOCK,
                                  merkle_root=self.MERKLE_ROOT,
                                  time=self.TIMESTAMP,
                                  bits=self.BITS,
                                  nonce=self.NONCE)

        assert bbhh.calculate_hash() == self.BLOCK_HASH

    '''
    TEST VERSION
    '''
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



