#-*-:coding:utf-8-*-
from sys import argv
from parser import *

result = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title> Pruebas</title>
</head>
<body>
<p>Fórmula generada:</p>
<div>''' + convert(argv[1]) + '''</div>
</body>
</html>'''

page = open('Prueba.html', 'w')
page.write(result)
page.close()


