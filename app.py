from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        health_data = {
            "status": "healthy",
            "service": "kubernetes-local-deployment",
            "environment": "production-mock"
        }
        self.wfile.write(json.dumps(health_data, indent=2).encode('utf-8'))

def run():
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print("Starting web server on port 8080...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()