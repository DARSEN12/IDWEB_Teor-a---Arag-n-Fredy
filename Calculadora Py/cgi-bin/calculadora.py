#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
expr = form.getvalue("expr", "")

print("<html><head><title>Resultado</title></head><body>")
print("<h1>Resultado de la Calculadora</h1>")

if expr:
    try:
        # Sanitizar entrada
        safe_expr = html.escape(expr)
        resultado = eval(expr)
        print(f"<p>Expresión: {safe_expr}</p>")
        print(f"<p>Resultado: {resultado}</p>")
    except Exception as e:
        print(f"<p>Error al calcular: {e}</p>")
else:
    print("<p>No se recibió ninguna expresión.</p>")

print("</body></html>")