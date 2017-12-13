'#--:coding:utf-8--'
from blindtex.converter import parser
import pytest



def test_convert():
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("a^b")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("a^{b}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a^b_c")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a^{b}_c")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a^{b}_{c}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a^b_{c}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a^{b}_{c}")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a_b")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("a_{b}")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("a_b^c")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("a_{b}^c")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("a_{b}^{c}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("{a}^b")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("{a}^{b}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}^b_c")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}^{b}_c")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}^{b}_{c}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}^b_{c}")
	assert 'a <span aria-label="s&uacute;per">&nbsp;</span>b <span aria-label="fin s&uacute;per">&nbsp;</span><span aria-label="sub">&nbsp;</span>c <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}^{b}_{c}")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}_b")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span> ' == parser.convert("{a}_{b}")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("{a}_b^c")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("{a}_{b}^c")
	assert 'a <span aria-label="sub">&nbsp;</span>b <span aria-label="fin sub">&nbsp;</span><span aria-label="s&uacute;per">&nbsp;</span>c <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert("{a}_{b}^{c}")
	assert '<span aria-label="comienza fracci&oacute;n">&nbsp;</span>a <span aria-label="sobre">&nbsp;</span>b <span aria-label="fin fracci&oacute;n">&nbsp;</span> ' == parser.convert("\\frac ab")
	assert '<span aria-label="comienza fracci&oacute;n">&nbsp;</span>a <span aria-label="sobre">&nbsp;</span>b <span aria-label="fin fracci&oacute;n">&nbsp;</span> ' == parser.convert("\\frac{a}{b}")
	assert '<span aria-label="comienza fracci&oacute;n">&nbsp;</span>a <span aria-label="sobre">&nbsp;</span>b <span aria-label="fin fracci&oacute;n">&nbsp;</span> ' == parser.convert("\\frac{a}b")
	assert '<span aria-label="comienza fracci&oacute;n">&nbsp;</span>a <span aria-label="sobre">&nbsp;</span>b <span aria-label="fin fracci&oacute;n">&nbsp;</span> ' == parser.convert("\\frac a{b}")
	assert '<span aria-label="ra&iacute;z cuadrada de">&nbsp;</span>a <span aria-label="termina ra&iacute;z">&nbsp;</span> ' == parser.convert("\\sqrt{a}")
	assert '<span aria-label="ra&iacute;z cuadrada de">&nbsp;</span>a <span aria-label="termina ra&iacute;z">&nbsp;</span> ' == parser.convert("\\sqrt a")
	assert '<span aria-label="ra&iacute;z">&nbsp;</span>b <span aria-label="de">&nbsp;</span>a <span aria-label="termina ra&iacute;z">&nbsp;</span> ' == parser.convert("\\sqrt[b]{a}")
	assert '<span aria-label="ra&iacute;z">&nbsp;</span>b <span aria-label="de">&nbsp;</span>a <span aria-label="termina ra&iacute;z">&nbsp;</span> ' == parser.convert("\\sqrt[b]a")
	assert 'a <span aria-label="m&aacute;s">&nbsp;</span>b  ' == parser.convert("a+b")
	assert 'a <span aria-label="producto">&nbsp;</span>b  ' == parser.convert("a\\times b")
	assert 'a <span aria-label="igual">&nbsp;</span>b  ' == parser.convert("a=b")
	assert 'a <span aria-label="menor igual">&nbsp;</span>b  ' == parser.convert("a\\leq b")
	assert 'a <span aria-label="no">&nbsp;</span><span aria-label="menor">&nbsp;</span>b  ' == parser.convert("a\\not< b")
	assert 'a <span aria-label="no">&nbsp;</span><span aria-label="equivalente">&nbsp;</span>b  ' == parser.convert("a\\not\\equiv b")
	assert '<span aria-label="seno">&nbsp;</span> ' == parser.convert("\\sin")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum_a^b")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum_a^{b}")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum_{a}^b")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum _{a}^{b}")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum^b_a")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum^b_{a}")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum^{b}_a")
	assert '<span aria-label="suma desde">&nbsp;</span>a <span aria-label="hasta">&nbsp;</span>b <span aria-label="de">&nbsp;</span> ' == parser.convert("\\sum^{b}_{a}")
	assert '<span aria-label="integral">&nbsp;</span> ' == parser.convert("\\int")
	assert '<span aria-label="integral sobre">&nbsp;</span>a <span aria-label="de">&nbsp;</span> ' == parser.convert("\\int_a")
	assert '<span aria-label="integral sobre">&nbsp;</span>a <span aria-label="de">&nbsp;</span> ' == parser.convert("\\int_{a}")
	assert 'a <span aria-label="flecha izquierda">&nbsp;</span>b  ' == parser.convert("a\\leftarrow b")
	assert '<span aria-label="abre par&eacute;ntesis">&nbsp;</span>a <span aria-label="cierra par&eacute;ntesis">&nbsp;</span> ' == parser.convert("(a)")
	assert '<span aria-label="abre llave">&nbsp;</span>a <span aria-label="cierra llave">&nbsp;</span> ' == parser.convert("\\{a\\}")
	assert '<span aria-label="abre corchete">&nbsp;</span>a <span aria-label="cierra corchete">&nbsp;</span> ' == parser.convert("\\left[a\\right]")
	assert 'a <span aria-label="gorro">&nbsp;</span> ' == parser.convert("\\hat a")
	assert 'a <span aria-label="gorro">&nbsp;</span> ' == parser.convert("\\hat{a}")
	assert '<span aria-label="gorro">&nbsp;</span>a <span aria-label="m&aacute;s">&nbsp;</span>b <span aria-label="fin gorro">&nbsp;</span> ' == parser.convert("\\hat{a+b}")
	assert '<span aria-label="it&aacute;lica">&nbsp;</span>a <span aria-label="fin it&aacute;lica">&nbsp;</span> ' == parser.convert("\\mathit a")
	assert '<span aria-label="it&aacute;lica">&nbsp;</span>a <span aria-label="fin it&aacute;lica">&nbsp;</span> ' == parser.convert("\\mathit{a}")
	assert '<span aria-label="puntos centrados">&nbsp;</span> ' == parser.convert("\\cdots")
	assert '<span aria-label="l&iacute;mite de">&nbsp;</span> ' == parser.convert("\\lim")
	assert '<span aria-label="l&iacute;mite cuando">&nbsp;</span>a <span aria-label="de">&nbsp;</span> ' == parser.convert("\\lim_a")
	assert '<span aria-label="l&iacute;mite cuando">&nbsp;</span>a <span aria-label="de">&nbsp;</span> ' == parser.convert("\\lim_{a}")
	assert '<span aria-label="mycommand">&nbsp;</span> ' == parser.convert("\\mycommand")

#Function to test miscellaneous formulas, some previously have presented problems.
def test_miscConvert():
	assert 'a b <span aria-label="s&uacute;per">&nbsp;</span>2 <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert('ab^2')
	assert '<span aria-label="parcial">&nbsp;</span> t <span aria-label="s&uacute;per">&nbsp;</span>2 <span aria-label="fin s&uacute;per">&nbsp;</span> ' == parser.convert('\\partial t^2')
