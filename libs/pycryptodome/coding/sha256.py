'''
	Get SHA256 hash of a string

'''

from Crypto.Hash import SHA256
h = SHA256.new()							# new Hash object

address = "490, first floor, \nSector 98, Mohali, \nPunjab-160098"

h.update(bytes(address, 'utf-8'))			# parse address in bytes with utf-8 encoding
print(type(h.hexdigest()))					# get hash | type - str