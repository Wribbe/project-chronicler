from setuptools import setup, find_packages

setup(
    name="rpgchronicler",
    author="Stefan Eng",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'rpgchronicler=rpgchronicler.app:run',
            'ping_rpgchronicler=rpgchronicler.app:ping',
        ]
    }
)
