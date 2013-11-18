from setuptools import setup, find_packages

setup(
    name = "hellobuildout",
    version = "1.0",
    url = 'https://github.com/soxofaan/hellobuildout',
    license = 'MIT',
    description = "Mimimal toy project to get the hang of Buildout.",
    author = 'Stefaan Lippens',
    # Search in the root folder for source file packages
    packages = find_packages('.'),
    # Define some console scripts, triggering functionality from the hellobuildout package.
    entry_points={
        'console_scripts': [
            'hellobuildout = hellobuildout:hello_buildout',
            'helloworld = hellobuildout:hello_world',
        ],
    },
)
