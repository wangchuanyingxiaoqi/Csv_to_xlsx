#! /usr/bin/python3

import argparse
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import Binary, Int64


def insert_tag(tag_collection, tag_num):
    tags = [
        {
            "_id": ObjectId(),
            "tag_name": "tag_{}".format(tag_id),
            "meta": {
            },
            "create_time": 0,
            "count": 0,
            "visible_identity": [
                0
            ],
            "_class": "com.ficus.face.product.park.core.tag.Tag"
        } for tag_id in range(tag_num)
    ]

    tag_collection.insert_many(tags)
    return [str(tag['_id']) for tag in tags]


def parse_args():
    parser = argparse.ArgumentParser(description='''
        该脚本用于批量导入标签
    ''')

    parser.add_argument('--tag_num', help='标签数量', type=int, required=True)
    parser.add_argument('--mongo_ip', help='mongodb地址', type=str, default='127.0.0.1')
    parser.add_argument('--mongo_port', help='mongodb端口', type=int, default=27017)
    parser.add_argument('--username', help='', type=str, default='park')
    parser.add_argument('--password', help='mongodb用户名', type=str, default='12345678')

    args = parser.parse_args()

    # assert not check_port_is_open(args.mongo_ip, 9812), 'stop park all'
    # assert check_port_is_open(args.mongo_ip, args.mongo_port), 'expose mongodb port'

    return args


# def main():
#     args = parse_args()
#
#     with MongoClient(args.mongo_ip, args.mongo_port, username=args.username, password=args.password,
#                      authSource='park') as mongo_client:
#         park = mongo_client.park
#         tags = insert_tag(park.tag, args.tag_num)
#         print(tags)

def main():

    with MongoClient("10.40.50.69", 27017, "park", "12345678") as mongo_client:
        park = mongo_client.park
        tags = insert_tag(park.tag, 10)
        print(tags)



if __name__ == '__main__':
    main()
