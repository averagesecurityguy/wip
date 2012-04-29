import httplib
conn = httplib.HTTPConnection("johntune.com")
conn.request("DELETE", "/davtest_yZJRyGi0ET9f9Vy.jsp")
r1 = conn.getresponse()
print r1.status, r1.reason
print r1.read()
