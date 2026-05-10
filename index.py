from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        q = parse_qs(urlparse(self.path).query)
        t = q.get('t', [''])[0]
        
        if not t:
            res = {'err': 'no text'}
        else:
            res = {
                'txt': t,
                'len': len(t),
                'words': len(t.split()),
                'up': t.upper()
            }
            
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(res).encode())
