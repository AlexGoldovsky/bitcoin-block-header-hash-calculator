from flask import Blueprint, jsonify, request
from BitBlockHeaderHash import BitBlockHeaderHash


bp_api = Blueprint('api', __name__)


@bp_api.route('/hash')
@bp_api.route('/')
def hash():
    version = int(request.args.get("version", 0))
    previous_block_hash=request.args.get("pbh", "")
    merkle_root=request.args.get("mr", "")
    time=int(request.args.get("timestamp", 0))
    bits=int(request.args.get("bits", 0))
    nonce=int(request.args.get("nonce", 0))

    bbhh = BitBlockHeaderHash(version=version,
                              previous_block_hash=previous_block_hash,
                              merkle_root=merkle_root,
                              time=time,
                              bits=bits,
                              nonce=nonce)
    return jsonify(
        hash=bbhh.calculate_hash()
    )
