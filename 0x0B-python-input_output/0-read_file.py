#!/usr/bin/python3
""" This module that contains a function which reads from a file """

def read_file(filename=""):
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
