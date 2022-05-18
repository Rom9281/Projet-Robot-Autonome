import http.server
from logging.handlers import SocketHandler
import socketserver

port = 3080
address = ("", port)

server = http.server.HTTPServer
server.
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/view"]

httpd = socketserver.TCPServer(address, handler)

print(f"Server demarré sur le port : {port}")

httpd.serve_forever()


