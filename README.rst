Django Project for my Website
=============================

Not of much use for other people.

As the website is public, the sources may be public, too.

I just collect some admin commands here to assist myself.

PDF to JPG
..........

High quality for certificates::

    gs -sDEVICE=jpeg -dJPEGQ100 -r300 -odocument.jpg document.pdf


Install and update my blogs
---------------------------

    # clone
    python manage.py sphinx clone TYPO3.Blog --ulr https://github.com/elmar-hinz/TYPO3.Blog.git

    # pull from git
    python manage.py sphinx pull TYPO3.Blog

    # build pickles
    python manage.py sphinx build TYPO3.Blog

    # build static website
    python manage.py sphinx publish TYPO3.Blog

    # pull, build, publish
    python manage.py update TYPO3.Blog


Install and update my python packages
-------------------------------------


