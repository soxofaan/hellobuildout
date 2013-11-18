
Hello Buildout
==============

This is a minimal toy project to get the hang of how Buildout works.
It is basically a simple module with tests and some metadata/configuration
(```setup.py``` and ```buildout.cfg```) to get things rolling.


Why?
----

I wanted to learn about Buildout, but it was a frustrating quest to find
well structured, to the point information and tutorials.
The article/tutorial that helped me most, after wading through numerous others, was
[Developing Django apps with zc.buildout by Jacob Kaplan-Moss](http://jacobian.org/writing/django-apps-with-buildout/).

This project was a dummy project to play with and better understand Buildout.
I hope that by sharing it, I make the make the road to understanding Buildout for one or two people a bit easier.


What's included?
----------------

Here's a short overview of the "source" files in this projects and where they come from.


* ```hellobuildout```: simple Python module for saying hello and a bit of tests for that.

* ```bootstrap.py```: this is Buildout's bootstrap script, downloaded with:

    ```
    wget http://downloads.buildout.org/2/bootstrap.py
    ```

* ```buildout.cfg```: minimal skeleton was first generated with:

    ```
    python bootstrap.py init
    ```

    After that, some more "parts" where added.

* ```setup.py```: standard setup script that describes the hellobuildout package and its related console scripts

* ```.gitignore```: includes some output files/folders from Buildout/setuptools to better not put in version control


What to do with it?
-------------------

1. Bootstrap Buildout (sets up basic buildout folder structure):

    ```python bootstrap.py```

2. Run Buildout (fetches dependencies, and puts some requested scripts into `bin/`):

    ```./bin/buildout```

3. Run the generated scripts

    ./bin/helloworld
    ./bin/hellobuildout
    ./bin/test


