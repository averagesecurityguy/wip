#!/usr/bin/env python

import cherrypy

class Cookie:
	
	def index(self, c=None):
		return "<h1>" + c + "</h1>"
		
	index.exposed = True

if __name__ == "__main__":
	cherrypy.quickstart(Cookie())
