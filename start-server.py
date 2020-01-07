from __future__ import print_function
import http.server
import socketserver

PORT = 8000 #This will serve at port 8080 

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
