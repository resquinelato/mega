# -*- coding: utf-8 -*-
# mega.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" 
Tutorial Dois - Brincando de git.

.. codeauthor:: Rodrigo Esquinelato <resquinelato@gmail.com>

- Como criar um repositório no github
- Como clonar usando o comando git
   - git clone url.do.repositório
- Como comitar usando o comando git
   - git commit -am "mensagem a comitar"

Classes neste modulo:

    :py:class:`Main` Exemplo de classe qualquer.

Changelog
---------

.. versionadded::    20.07

        Documentação do tutorial.
"""


class Main:
    """Classe exemplo:

       :param versao: versao desse exemplo.

    """
    def __init__(self, versao = "20.07"):
        self.versao = versao
        print ("Classe exemplo, versão {}".format(versao))

    def get_versao(self):
        '''Retorna a versão do sistema.

           :return: A versão do sistema
        '''
        return self.versao

if __name__ == "__main__":
    print(Main().get_versao())
