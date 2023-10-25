import http.server
import socketserver
import datetime

#http://127.0.0.1:8000/
#ngrok
# Classe personalizada para manipular solicitações
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Obter o endereço IP do cliente
            client_address = self.client_address[0]

            # Obter a data e hora atuais
            current_time = datetime.datetime.now()

            # Criar a página HTML dinâmica
            html = f"""
            <html>
            <head><title>Informacoes Dinamicas</title></head>
            <body>
                <h1>Informacoes Dinamicas</h1>
                <p>Endereço IP do cliente: {client_address}</p>
                <p>Data e hora atuais: {current_time}</p>
            </body>
            </html>
            """

            self.wfile.write(html.encode('utf-8'))
        else:
            # Se a URL não for reconhecida, retorne um erro 404
            self.send_response(404)
            self.end_headers()

# Configurar o servidor para escutar na porta 8000
with socketserver.TCPServer(('', 8000), MyHandler) as httpd:
    print('Servidor ativo na porta 8000...')
    httpd.serve_forever()
