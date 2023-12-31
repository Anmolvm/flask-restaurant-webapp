from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                message = ""
                message += "<html><body>Hello!</body></html>"
                self.wfile.write(message)
                print(message)
                return
            else:
                self.send_error(404, 'File Not Found: %s' % self.path)
        except Exception as e:
            print(e)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web server running at port %s", port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("stopping the server")
        server.socket.close()


if __name__ == '__main__':
    main()
