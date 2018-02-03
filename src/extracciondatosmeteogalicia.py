#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "pablovilches"
try:
    from bs4 import BeautifulSoup
    from urllib2 import Request
except ValueError:
    print("Hubo problemas de importacion " + ValueError)
    
# CREAMOS LA CLASE Extraccion   
class Extraccion:
    ## CAPTURAMOS LA URL INGRESADA EN LA VARIABLE "url".
    url = raw_input("Ingrese la URL: ")

    ## CAPTURAMOS EL HTML DE LA PÁGINA WEB Y CREAMOS UN OBJETO RESPONSE.
    r = request.get("http://" +url)
    data = r.text
    print ""

    ## CREAMOS EL OBJETO SOUP Y LE PASAMOS LO CAPTURADO CON REQUEST.
    soup = BeautifulSoup(data,'lxml')

    ## CAPTURAMOS EL TÍTULO DE LA PÁGINA Y LUEGO LO MOSTRAMOS. LO QUE HACE BEAUTIFULSOUP ES CAPTURAR LO QUE ESTÁ 
    ## DENTRO DE LA
    ## ETIQUETA TITLE DE LA URL.
    titulo = soup.title.text
    print "El título de la página es: " + titulo
    print ""

    ## BUSCAMOS TODAS ETIQUETAS HTML(a) Y LUEGO IMPRIMIMOS 
    ## todo LO QUE VIENE DESPUÉS DE "href".
    for link in soup.find_all('a'):
        print(link.get('href'))
    
if __name__ == "__main__":
    main = extraccion()
    Gtk.main()