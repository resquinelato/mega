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

@route('/')
def hello_world():
    return 'Tutorial Dois - Aprendendo Git e Botlle'

@route('/oi')
def oi_mundo():
    return 'Tutorial Dois - Ensaiando uma nova rota'

application = default_app()

