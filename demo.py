import urllib2
response = urllib2.urlopen("http://www.facebook.com")
print "-" * 20
print "URL : ", response.geturl()

headers = response.info()
print "-" * 20
print "This prints the header: ", headers
print "-" * 20
print "Date :", headers['date']
print "-" * 20
print "Server Name: ", headers['Server']
print "-" * 20
print "Last-Modified: ", headers['Last-Modified']
print "-" * 20
print "ETag: ", headers['ETag']
print "-" * 20
print "Content-Length: ", headers['Content-Length']
print "-" * 20
print "Connection: ", headers['Connection']
print "-" * 20
print "Content-Type: ", headers['Content-Type']
print "-" * 20
