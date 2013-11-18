
Hello Buildout
==============

This is a minimal toy project to get the hang of how [Buildout](http://www.buildout.org/) works.
It is basically a simple Python module with tests and some metadata/configuration
(```setup.py``` and ```buildout.cfg```) to get things rolling.


Why?
----

I wanted to learn about Buildout, but it was a frustrating quest to find
well structured, to the point information and tutorials.
The article/tutorial that helped me most, after wading through numerous others, was
[Developing Django apps with zc.buildout by Jacob Kaplan-Moss](http://jacobian.org/writing/django-apps-with-buildout/).

This project was a dummy project to play with and better understand Buildout.
I hope that by sharing it, I make the road to understanding Buildout a bit less bumpy for one or two people.


What's included?
----------------

Here's a short overview of the "source" files in this projects and where they come from.


* `hellobuildout`: simple Python package for saying hello and a bit of tests for that.

* `bootstrap.py`: this is Buildout's bootstrap script, just downloaded as follows:

    ```
    wget http://downloads.buildout.org/2/bootstrap.py
    ```

* `buildout.cfg`: the initial version of this Buildout configuration skeleton was generated as follows:

    ```
    python bootstrap.py init
    ```

    After that, some more Buildout "parts" where added manually.

* `setup.py`: standard `setup.py` script that describes the hellobuildout package and its related console scripts.

* `.gitignore`: includes some output files/folders from Buildout/setuptools, which you better not put in your VCS.


What to do with it?
-------------------

1. Bootstrap Buildout (sets up basic buildout folder structure):

    ```
    python bootstrap.py
    ```

2. Run Buildout (fetches dependencies, and puts some requested scripts into `bin/`):

    ```
    ./bin/buildout
    ```

3. Run the generated scripts

    ```
    ./bin/helloworld
    ./bin/hellobuildout
    ./bin/test
    ```


More info
---------

Look in `buildout.cfg` and `setup.py` for a bit more information and configuration details.

