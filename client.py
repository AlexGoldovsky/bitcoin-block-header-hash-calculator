from BitBlockHeaderHash import BitBlockHeaderHash

bbhh = BitBlockHeaderHash(version=3,
                          previous_block_hash="0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6",
                         merkle_root="f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db",
                         time=1442663985,
                         bits=403867578,
                         nonce=3548193207)

print bbhh.calculate_hash()


