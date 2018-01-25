#!/usr/bin/python

import click
from BitBlockHeaderHash import BitBlockHeaderHash


@click.group()
def cli():
    pass

@cli.command()
@click.option('--verbose', is_flag=True, help='Verbose output - Flag.')
@click.option('--version', prompt='Version', help='Version.', type=int)
@click.option('--mr', "merkle_root", prompt='Merkle Root', help='Merkle Root.')
@click.option('--time', prompt='Unix Timestamp', help='Unix Timestamp.', type=int)
@click.option('--bits', prompt='Bits', help='Bits.', type=int)
@click.option('--nonce', prompt='Nonce', help='Nonce.', type=int)
@click.option('--pbh', "previous_block_hash", prompt='Previous Block Hash', help='Previous Block Hash.')
def hash(version, previous_block_hash, merkle_root, time, bits, nonce, verbose):

    bbhh = BitBlockHeaderHash(version=version,
                                  previous_block_hash=previous_block_hash,
                                  merkle_root=merkle_root,
                                  time=time,
                                  bits=bits,
                                  nonce=nonce)

    hashed=bbhh.calculate_hash()
    if verbose:
        print_introduction(version, previous_block_hash, merkle_root, time,
                           bits, nonce)

        click.echo("The Hash is {}".format(hashed))
    else:
        click.echo(hashed)



@cli.command()
def example():
    version=3
    previous_block_hash="0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6"
    merkle_root="f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db"
    time=1442663985
    bits=403867578
    nonce=3548193207

    print_introduction(version, previous_block_hash, merkle_root, time,
                       bits, nonce)

    bbhh = BitBlockHeaderHash(version=version,
                              previous_block_hash=previous_block_hash,
                              merkle_root=merkle_root,
                              time=time,
                              bits=bits,
                              nonce=nonce)
    click.echo("The Hash is {}".format(bbhh.calculate_hash()))


def print_introduction(version, previous_block_hash, merkle_root, time, bits, nonce):
    click.echo("Calculating Block Header Hash for the following values:\nVersion - {}\nPrevious Block Hash - {}\nMerkle Root - {}\nTime - {}\nBits - {}\nNonce - {}".format(version, previous_block_hash, merkle_root, time, bits, nonce))

if __name__ == "__main__":
    cli()
