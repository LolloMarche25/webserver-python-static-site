# -*- coding: utf-8 -*-
# Corso di Programmazione di Reti - UniversitÃ  di Bologna
# Traccia 1 - Realizzazione di un sito web statico

import os
import mimetypes
import logging
from socket import *

logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Il server deve rispondere su localhost:8080
serverPort=8080
serverSocket = socket(AF_INET, SOCK_STREAM)
server_address=('localhost',serverPort)
serverSocket.bind(server_address)

#listen(1) Definisce la lunghezza della coda di backlog
serverSocket.listen(1)
print ('The web server is up on port:',serverPort)

while True:

    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("Connection from:", addr)
    logging.info(f"Connection from: {addr}")

    try:
        message = connectionSocket.recv(1024).decode()
        print("Message received:", message)
        
        # Gestione delle richieste GET
        
        if len(message.split())>0 and message.startswith('GET'): 
            method = message.split()[0]
            filename = message.split()[1]
            print (f"Method: {method},Filename: {filename}")
            logging.info(f"Request: {method} {filename}")
            
            if filename == "/":
                filename = "/index.html"
                
            filepath = "www" + filename  # Cartella del file del sito
            print("Try to open:", filepath)
            
            # Gestione dei MIME types
            mime_type, _= mimetypes.guess_type(filepath)
            if mime_type is None:
                mime_type = "application/octet-stream"
                
            with open(filepath, 'rb') as f:
                outputdata = f.read()
            
                
     # Risposta HTTP 200 con MIME type

            header = (
                f"HTTP/1.1 200 OK\r\n"
                f"Content-Type: {mime_type}; charset=utf-8\r\n"
                "\r\n"
            )
            connectionSocket.send(header.encode())
            connectionSocket.send(outputdata)
            connectionSocket.send("\r\n".encode())
                
        connectionSocket.close()
            
    # Risposta 404 per file inesistenti
    
    except FileNotFoundError:
        logging.warning(f"File Not Found: {filepath}")
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
        connectionSocket.close()
    
    except Exception as e:
        print("Generic Error:", e)
        logging.error(f"Generic Error: {e}")
        connectionSocket.close()

