# -*- coding: utf-8 -*-
# bottle_app.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Tutorial Dois - Brincando de git.

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

Sem classes neste modulo:

Changelog
---------
.. versionadded::    20.07
        Adiciona o gerencidor de comandos http via Bottle
"""

from bottle import default_app, route
from main import Main
from bottle import static_file

@route('/')
def hello_world():
    return 'Tutorial Dois - Aprendendo Git e Botlle'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - Ensaiando uma nova rota'

@route('/vs')
def vs_mundo():
    """Roteia o caminho /vs para retornar a versão do sistema."""
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/resquinelato/dev/mega/docs/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/resquinelato/dev/mega/docs/build/html/', mimetype='text/css')



application = default_app()

