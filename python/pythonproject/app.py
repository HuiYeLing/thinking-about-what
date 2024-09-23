# -*- coding: utf-8 -*-
# File : scheduler2.py.py
# Author: taoyahui
# Date : 2022/3/21
from models import Transaction, Blockchain, Peer
from datetime import datetime
from flask import Flask, request, jsonify
import crypto_util
import utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 空数据返回内容
empty_res = {
    'code': 404,
    'data': 'empty'
}

# 执行成功返回内容
success_res = {
    'code': 200,
    'data': 'ok'
}

# 创建区块链
blockchain = Blockchain()

# 创建一个模拟节点
peer = Peer()

@app.route("/account_create", methods=['GET'])
def account_create():
    """
    创建账户接口
    :return:
    """
    return jsonify({
        'code':200,
        'data':crypto_util.create_account()
    })


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    """
    新增一笔交易
    :return:
    """
    body = request.json
    if 'sender' not in body or 'recipient' not in body \
            or 'data' not in body or 'private_key' not in body:
        return jsonify(empty_res)
    new_transaction = Transaction(body['sender'],
                                  body['recipient'],
                                  body['data'],
                                  datetime.now(),
                                  body['private_key'])
    peer.tx_pool.append(new_transaction)
    return jsonify(success_res)


@app.route('/add_block', methods=['GET'])
def add():
    """
    添加新区块接口,将peer节点的交易缓存数据加入新区块中
    :return:
    """
    tx_list = peer.tx_pool
    index = blockchain.add_new_block(tx_list)
    peer.tx_pool = []
    # 数据返回内容，在data中加入新加入区块的索引
    return jsonify({
        'code': 200,
        'data': index
    })


@app.route('/query_block', methods=['GET'])
def query_block():
    """
    区块查询接口，通过HTTP GET方法接收查询区块的索引
    请求示例如: http://127.0.0.1:5000/query?index=0
    :return:
    """
    index = int(request.args['index'])
    # 数据返回内容，返回查询区块的完整信息
    return jsonify({
        'code': 200,
        'data': blockchain.query_block_info(index)
    })


@app.route('/query_tx', methods=['GET'])
def query_tx():
    """
    查询交易接口
    :return:
    """
    id = request.args['id']
    for block in blockchain.chain:
        for tx in block.data:
            if tx.id == id:
                return jsonify({
                    'code': 200,
                    'data': tx.to_json()
                })
    return jsonify({
        'code': 404,
        'data': '未查询到相关交易'
    })


@app.route('/validate_tx', methods=['POST'])
def validate_tx():
    """
    验证交易接口,需要通过POST传递交易哈希(id)和公钥(public_key)
    :return:
    """
    res_json = request.json
    if 'id' not in res_json or 'public_key' not in res_json:
        return jsonify(empty_res)
    tx_id = res_json['id']
    for block in blockchain.chain:
        for tx in block.data:
            if tx.id == tx_id:
                verification_res = \
                    crypto_util.data_verify(tx.id, tx.sig, res_json['public_key'])
                if verification_res == 0:
                    return jsonify({
                        'code': 200,
                        'data': '验证成功'
                    })
                else:
                    return jsonify({
                        'code': 500,
                        'data': '验证失败！'
                    })

@app.route('/validate_block', methods=['GET'])
def validate_block():
    """
    验证区块接口
    :return:
    """
    index = int(request.args['index'])
    block = blockchain.chain[index]
    root = block.merkle_root
    calc_root = utils.calc_merkle_root(block.data)
    if root == calc_root:
        return jsonify({
            'code': 200,
            'data': 'ok'
        })
    else:
        return jsonify({
            'code': 500,
            'data': '结果不符！'
        })


if __name__ == '__main__':
    app.run(port=5001)
