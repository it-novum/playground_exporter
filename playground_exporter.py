# Python 3 playground_exporter for Prometheus
# This exporter only exists for testing purpose 
# It has no real use case!
#
# MIT License

from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import urllib.parse

http_port = 9999

class PlaygroundExporter(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        query_params = urllib.parse.parse_qs(self.path)


        if(self.path.startswith("/metrics")):
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes("# HELP current_random_value is a random number.\n", "utf-8"))
            self.wfile.write(bytes("# TYPE current_random_value gauge\n", "utf-8"))
            self.wfile.write(bytes("current_random_value {}\n".format(random.random()), "utf-8"))

            if("apitoken" in query_params):
                if query_params["apitoken"][0] == "secret123":
                    self.wfile.write(bytes("# HELP protected_secret_value is a protected number and require a apitoken.\n", "utf-8"))
                    self.wfile.write(bytes("# TYPE protected_secret_value gauge\n", "utf-8"))
                    self.wfile.write(bytes("protected_secret_value {}\n".format(random.randint(1, 100)), "utf-8"))


            # End /metrics route
            return


        # Default route 
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Playground Exporter</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<h1>Playground Exporter</h1><p><a href='/metrics'>Metrics</a></p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    http_server = HTTPServer(("0.0.0.0", http_port), PlaygroundExporter)
    print("Server started http://%s:%s" % ("0.0.0.0", http_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass

    http_server.server_close()
    print("Exporter stopped.")

