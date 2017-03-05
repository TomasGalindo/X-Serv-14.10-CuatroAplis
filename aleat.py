#!/usr/bin/python3

import random


class url_aleat ():
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        num = random.randint(1, 9999999999999999)
        redirect = "http://localhost:1234/aleat/" + str(num)
        return ("200 OK", "<html><body><h1><a href= " + redirect +
                          ">Dame mas</a>" + "</h1></body></html>")
