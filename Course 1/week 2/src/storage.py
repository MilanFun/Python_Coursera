import argparse
import json
import os
import tempfile

# Read input command from console
parser = argparse.ArgumentParser('Key-value storage')
parser.add_argument('--key', dest='key',help='Key for value in storage')
parser.add_argument('--value', dest='value',help='Value which storage in file with his key')
args = parser.parse_args()

# Print what was read
# print("Map: {}: {}".format(args.key, args.value))

# Path to the file where will save value
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# print(storage_path)

if os.path.exists(storage_path):
    if args.value != None:
        with open(storage_path, 'r') as f:
            storage_dict = json.load(f)

        if args.key in storage_dict:
            tmp_list_of_value = storage_dict[args.key]
            tmp_list_of_value.append(args.value)
            storage_dict[args.key] = tmp_list_of_value
        else:
            storage_dict[args.key] = [args.value]

        with open(storage_path, 'w') as f:
            json.dump(storage_dict, f)
    else:
        with open(storage_path, 'r') as f:
            decoded_hand = json.load(f)

        if args.key in decoded_hand:
            print(', '.join(decoded_hand.get(args.key)))
        else:
            print(None)
else: 
    tmp_dict = dict()

    if args.value != None:
        tmp_dict[args.key] = [args.value]

        with open(storage_path, 'w') as f:
            json.dump(tmp_dict, f)
    else:
        print(None)
