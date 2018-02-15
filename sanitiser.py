#!/usr/bin/env python

"""
https://github.com/rsyslog/rsyslog/blob/master/plugins/external/messagemod/anon_cc_nbrs/anon_cc_nbrs.py
"""

import sys
import re
import json

def onInit():
	global rc
	global patterns
	patterns = {
	            '(^|[^A-Za-z0-9.])(\d+-\d+-\d+)([^A-Za-z0-9]|$)': 'XXX-XXX-XXXX'
	}
	rc = re.compile("("+")|(".join(patterns.keys())+")")


def onReceive(msg):

	global rc
	global patterns

	def lookup(match):
		for pat in patterns.keys():
			res = re.match(pat, match.group(0))
			if res:
				return str(res.group(1))+patterns[pat]+str(res.group(res.lastindex))
				break

	res_msg = rc.sub(lambda m: lookup(m), msg)
	if res_msg == msg:
		print json.dumps({'msg': res_msg})
	else:
		print json.dumps({'msg': res_msg})

"""
See also: https://github.com/rsyslog/rsyslog/issues/22
"""
onInit()
keepRunning = 1
while keepRunning == 1:
	msg = sys.stdin.readline()
	if msg:
		msg = msg[:-1] # remove LF
		onReceive(msg)
		sys.stdout.flush() # very important, Python buffers far too much!
	else: # an empty line means stdin has been closed
		keepRunning = 0

sys.stdout.flush() # very important, Python buffers far too much!
