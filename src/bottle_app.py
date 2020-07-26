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

from bottle import default_app, route, static_file
from main import Main


@route('/')
def hello_world():
    return static_file('index.html', root='/home/resquinelato/dev/mega/src/', mimetype='text/html')

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - Ensaiando uma nova rota'

@route('/vs')
def vs_mundo():
    """Roteia o caminho /vs para retornar a versão do sistema."""
    return 'Tutorial Dois - Versão do sistema: {}'.format(Main().get_versao())

@route('/<filename:re:.*\.py>')
def py_mundo(filename):
    return static_file(filename, root='/home/resquinelato/dev/mega/src/', mimetype='text/python')

@route('/doc/<filename:re:.*\.html>')
def doc_mundo(filename):
    return static_file(filename, root='/home/resquinelato/dev/mega/docs/build/html', mimetype='text/html')

@route('/doc/<filename:re:.*\.css>')
def css_mundo(filename):
    return static_file(filename, root='/home/resquinelato/dev/mega/docs/build/html/', mimetype='text/css')



application = default_app()

