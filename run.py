# -*- coding: UTF-8 -*-
tld = open("tld.txt").read().splitlines()
sanat = open("parsed.txt").read().splitlines()

for sana in sanat:
	aakkos = sana.replace("ä", "a").replace("ö", "o").replace("å", "a")
	for t in tld:
		if sana.upper().endswith(t.upper()):
			print(sana.lower()[0:-len(t)] + "." + t.lower())
		elif aakkos.upper().endswith(t.upper()):
			print(aakkos.lower()[0:-len(t)] + "." + t.lower())
