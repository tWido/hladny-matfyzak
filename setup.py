from setuptools import setup

setup(
    name='hladny-matfyzak',

    version='0.0.5',

    description='Python parsing functions for hungry students in Bratislava',

    url='https://github.com/hladny-matfyzak/py-hladny-matfyzak',

    author='Wido',

    author_email='tomas.wido@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: API'
    ],

    install_requires=['requests', 'BeautifulSoup', 'enum34'],
)
