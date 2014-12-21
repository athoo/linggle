#!/usr/bin/env python
# -*- coding: utf-8 -*-
from heapq import heappush
from collections import defaultdict
import shelve
import argparse
import sys
import fileinput

def recursion(key, n ):
    if n >= 0:
        a_key = key[:]
        a_key[n] = '_'
        return [a_key] + recursion(a_key, n-1) + recursion(key[:], n-1)
    return []

def mapper(files):
	for line in fileinput.input(files):
		line = line.strip()
		line = line.split('\t')
		key = line[0].split(' ')
		# print key
		value = line[1]
		# print key
		# print line[0]+"=>"+line[0]+'\t'+line[1]
		x= recursion(key,len(key)-1)

		for i in x:
			# print i
			# temp = key
			# temp[i]='_'
			# print " ".join(temp)
			print ' '.join(i)+"=>"+line[0]+'\t'+line[1]
			# print key
			# temp=key


def reducer(files):
	for item in fileinput.input(files):
		# print item
		key1 = item.split("=>")[0]
		key2 = item.split("=>")[1].split("\t")[0]
		value = item.split("=>")[1].split("\t")[1].strip()
		redu[key1][key2]=value
		# heappush(redu[key1],tuple([key2,value]))
	for key in redu:
		# for item in redu[key]:
			# ' '.join(map(str,item))
		# print key+"=>"+redu[key]
		temp=[]
		for key2 in redu[key]:
			temp.append(key2+'\t'+redu[key][key2])
		temp=sorted(temp,key=lambda item: int(item.split('\t')[1]),reverse=True)
		# temp.sort(key = lambda element int(temp.element('\t')[1]))
		print key+"=>"+",".join(temp)
		# print key1+"=>"+redu[key1]


		# print key1,redu[key1]
		# print key1,key2,value
	# for key in redu[key1]:



		# print redu[key1]

if __name__ == '__main__':
	redu = defaultdict(lambda : defaultdict(int))
	# redu = defaultdict(list)
	parser = argparse.ArgumentParser(description='N-gram counter')
	parser.add_argument('-r', '--reducer', action='store_true', help='reducer mode')
	parser.add_argument('-m', '--mapper', action='store_true', help='mapper mode')
	parser.add_argument('files', metavar='FILE', type=str, nargs='*', help='input files')
	args = parser.parse_args()
	if (args.mapper and args.reducer or not args.mapper and not args.reducer):
		parser.print_help()
		sys.exit(1)

	if args.mapper:
		mapper(args.files)
	elif args.reducer:
		reducer(args.files)
		# d=shelve.open('data.shelve')
		# for key in redu.keys():
		# 	d[key]=redu[key]
		# 	print d[key],redu[key]
		# d.close()
