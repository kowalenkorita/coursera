import os
import tempfile
import argparse
import json
# from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("--key", type=str)
parser.add_argument("--val", type=str)
args = parser.parse_args()
# print(args.key)
# print(args.val)

dictionary = {}
dicti = {}

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not (os.path.exists(storage_path)):
	f = open(storage_path, "w")
	# f.write(json.dumps(dictionary))

# storage_path = "hello.txt"

if args.key and args.val:
	with open(storage_path, 'r', encoding='utf-8') as f:
		data = f.read()
		if len(data) != 0:
			dictionary = json.loads(data)
		if args.key not in dictionary.keys():
			dictionary[args.key] = list()
			dictionary[args.key].append(args.val)
		else:
			if args.val not in dictionary[args.key]:
				# dictionary = defaultdict(list)
				dictionary[args.key].append(args.val)
			# 	print("new2")
			# else:
			# 	print("not new")

	with open(storage_path, 'w', encoding='utf-8') as f:
		f.write(json.dumps(dictionary))

elif args.key and not args.val:
	with open(storage_path, 'r', encoding='utf-8') as f:
		# вывод всех записей по ключу
		str = f.read()
		if len(str) != 0:
			dicti = json.loads(str)
		if args.key in dicti.keys():
			for i in dicti[args.key][:-1]:
				print(i, end = ", ")
			print(dicti[args.key][-1])
			# print(dicti[args.key])
else:
	print(None)
