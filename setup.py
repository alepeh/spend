from setuptools import setup

setup(
    name='spend',
    version='0.0.1',
    py_modules=['spend'],
    install_requires=[
        'Click',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'spend = spend/spend:cli',
        ],
    },
)