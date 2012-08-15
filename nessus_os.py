#!/usr/bin/env python
#-----------------------------------------------------------------------------
# 
#-----------------------------------------------------------------------------

import xml.etree.ElementTree
import sys
import re
import os.path

#------------------------------------
# Object to hold Nessus host items
#------------------------------------

def usage():
	print("nessus_os.py nessus_file")
	sys.exit()

##
# Take the filename and confirm that it exists, is not empty, and is a Nessus 
# file.
def open_nessus_file(filename):
	if not os.path.exists(filename):
		print("{0} does not exist.".format(filename))
		sys.exit()
		
	if not os.path.isfile(filename):
		print("{0} is not a file.".format(filename))
		sys.exit()
		
	# Load Nessus XML file into the tree and get the root element.		
	nf = xml.etree.ElementTree.ElementTree(file=filename)
	root = nf.getroot()
	
	# Make sure this is a Nessus v2 file
	if root.tag == 'NessusClientData_v2':
		return filename, root
	else:
		print("{0} is not a Nessus version 2 file.".format(filename))
		sys.exit()


##
# Extract host properties from the host_properties XML node.
def process_host_properties(host_properties):
	ip = ''
	os = 'Unknown'
	fqdn = ''
	for tag in host_properties.findall('tag'):
		if tag.attrib['name'] == 'host-ip':
			ip = tag.text
		if tag.attrib['name'] == 'operating-system':
			os = tag.text
		if tag.attrib['name'] == 'host-fqdn':
			fqdn = tag.text

	return ip, fqdn, os


#-------------------------#
# Begin the main program. #
#-------------------------#

hosts = []

t =  '<?xml version="1.0" ?>\n'
t += '<NessusClientData_v2>\n'

##
# Compiled regular expressions
xp = re.compile(r'Microsoft Windows XP', re.I)

##
# Process program arguments
if len(sys.argv) != 2:
	usage()
	
if sys.argv[1] == '-h':
	usage()
else:
	file_name, nessus = open_nessus_file(sys.argv[1])

##
# Find all the reports in the Nessus file
reports = nessus.findall('Report')

##
# Process each of the reports
for report in reports:
	report_name = report.attrib['name']
	print("Processing report {0}".format(report_name))
	t += '<Report name="{0}">\n'.format(report_name)
	
	# Process each host in the report
	report_hosts = report.findall('ReportHost')
	for host in report_hosts:

		hid, fqdn, os = process_host_properties(host.find('HostProperties'))

		if xp.search(os):
			print("Processing host {0}".format(hid))	
			t += xml.etree.ElementTree.tostring(host)
				
	t += '</Report>\n'

t += '<NessusClientData_v2>\n'

summary_file = file_name + "_xp.nessus"
print("Saving report to {0}".format(summary_file))
summary = open(summary_file, "w")
summary.write(t)
