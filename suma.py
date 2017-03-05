#!/usr/bin/python3


class sumador():

    hay_operando1 = False
    valor1 = 0

    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information."""

        recurso = rest[1:]
        print("REST = " + recurso)
        # Comprobar favicon
        if (recurso == "favicon.ico"):
            return "favicon"
            recvSocket.close()

        # Comprobar si es int
        try:
            valor = int(recurso)
        except ValueError:              # no es int
            print ("No se ha introducido un numero entero")
            return None
            recvSocket.close()

        return valor

    def process(self, parsedRequest):
        if (parsedRequest == "favicon"):
            return ("404 Not found", "<html><body>" +
                    "<h1>Not Found</h1></body></html>")

        if (parsedRequest is None):
            return("404 Not Found", "<html><body>" +
                   "Error introducir valor</body></html>")

        # Si llega aqui quiere decir que es un int

        if (self.hay_operando1):
            # todo lo referido al segundo operando
            valor2 = int(parsedRequest)
            suma = self.valor1 + valor2
            self.hay_operando1 = False
            return("200 OK", "<html><body>" +
                             str(self.valor1) +
                             "+" + str(valor2) +
                             "=" + str(suma) +
                             "</body></html>")
            recvSocket.close()
        else:
            # todo lo referido al primer operando (todavia no hay operando1)
            self.valor1 = int(parsedRequest)
            self.hay_operando1 = True
            return("200 OK", "<html><body>" +
                             "Primer numero introducido:" +
                             str(self.valor1) +
                             "</body></html>")
            recvSocket.close()
