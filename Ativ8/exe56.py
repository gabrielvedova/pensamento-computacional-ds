#!/usr/bin/python3
# Nome: Gabriel Silva Della Vedova
# Turma: 2A

# 56.Implemente uma função que verifique se uma dada string contém apenas caracteres ASCII.

def is_ascii_only(input_string):
    return input_string.isascii()

# Example usage


print('Hello, World!', is_ascii_only("Hello, World!"))
# escola: 埃斯科拉
print('埃斯科拉', is_ascii_only("埃斯科拉"))

# Output:
# Hello, World! True
# 埃斯科拉 False
