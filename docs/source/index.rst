.. Tutorial Dois documentation master file, created by
   sphinx-quickstart on Sat Jul 25 04:23:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem vindo ao Tutorial Dois de documentação!
===========================================

Subtítulo importate
===================

Um texto muito difícil de ser compreendido::

    print "olá mundo!"
    >> olá!

Guia:
^^^^^^^

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo:

   license
   help

Modulo Vitollino
----------------

.. note::
   Engenho de jogos do Superpython

.. automodule:: vitollino.main
   :members:
   :undoc-members:
   :platform: Web
   :synopsis: Engenho de Jogos

Modulo Quarto
-------------

.. note::
   Jogo do Quarto traduzido do Superpython.

.. automodule:: quarto
   :members:
   :undoc-members:
   :platform: Web
   :synopsis: Jogo do quarto.

Modulo Main
-----------

.. note::
   Só gera a versão.

.. automodule:: main
   :members:
   :undoc-members:
   :platform: Web
   :synopsis: Gera versão.

Modulo Gerenciador Http
------------------------

:/oi: diz oi
:/doc: mostra a documentação

.. automodule:: bottle_app
   :members:
   :undoc-members:
   :platform: Web
   :synopsis: Gerenciador http.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
