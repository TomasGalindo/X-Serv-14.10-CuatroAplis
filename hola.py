#!/usr/bin/python3
# importo webappmulti para usar el parse de la clase app
import webappmulti


class hola(webappmulti.app):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "HOLA!!" + "</h1></body></html>")


class adios(webappmulti.app):
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>" +
                          "ADIOS!!" + "</h1></body></html>")
