=============
 PyTagCloud
=============

PyTagCloud let you create simple tag clouds inspired by `Wordle <http://www.wordle.net/>`_.

This is a fork of `the original PyTagCloud <https://github.com/atizo/PyTagCloud>`_, that aims to support Korean.
(A `pull request <https://github.com/atizo/PyTagCloud/pull/19>`_ has been sent to the original as of Jun 11, 2014.)

Currently, the following output formats have been written and are working:

- PNG images
- HTML/CSS code


Requirements
============

#. Install `pygame <http://www.pygame.org/download.shtml>`_ >= 1.9.1::

    $ apt-get install python-pygame
    
#. Install simplejson::

   $ pip install simplejson


Installation
============

Try::

    # pip install git+https://github.com/e9t/PyTagCloud.git

or::

    $ git clone git@github.com:e9t/PyTagCloud.git
    $ cd PyTagCloud
    # python setup.py install


Examples
========

- `국회 발의 의안 워드클라우드 그리기 <https://github.com/e9t/konlpy/wiki/Ex:-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B7%B8%EB%A6%AC%EA%B8%B0>`_::

.. image:: https://raw.githubusercontent.com/e9t/konlpy/master/examples/wordcloud.png
