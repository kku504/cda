#!/usr/bin/env python

import whois

data = raw_input("Enter a domain: ")
w = whois.whois(data)

print w
