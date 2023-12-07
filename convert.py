import json
from google.protobuf.json_format import ParseDict
from Ct_pb2 import CtRoot

def json_to_pbf(json_data):
    protobuf_message = CtRoot()
    ParseDict(json_data, protobuf_message)
    return protobuf_message

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def write_pbf(file_path, protobuf_message):
    with open(file_path, 'wb') as pbf_file:
        pbf_file.write(protobuf_message.SerializeToString())

if __name__ == "__main__":
    json_data = read_json("sample.json")
    protobuf_message = json_to_pbf(json_data)
    write_pbf("sample.pbf", protobuf_message)