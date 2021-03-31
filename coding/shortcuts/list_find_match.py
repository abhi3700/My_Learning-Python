# the list
'''

	Original list =  ['CLMUV1','REOX1B','CLREPL1','ASFE1','CLREML1','REPL1B','REOX1A','RESP1A','ASBE1',
						'REML1C,ASBE1','ASFE1,ASBE1','REPL1A','REML1C','ASBE1,REML1C','CLFRBG1',
						'CLREOX1','RESP1B','REOX1C','CLRESP1','REML1A']

	New list = ['ASBE1', 'REML1C,ASBE1', 'ASFE1,ASBE1', 'ASBE1,REML1C']

'''

equip_list_unique = ['CLMUV1',
 'REOX1B',
 'CLREPL1',
 'ASFE1',
 'CLREML1',
 'REPL1B',
 'REOX1A',
 'RESP1A',
 'ASBE1',
 'REML1C,ASBE1',
 'ASFE1,ASBE1',
 'REPL1A',
 'REML1C',
 'ASBE1,REML1C',
 'CLFRBG1',
 'CLREOX1',
 'RESP1B',
 'REOX1C',
 'CLRESP1',
 'REML1A']


asbe1_equip_names = [e for e in equip_list_unique if "ASBE1" in e]
print(asbe1_equip_names)