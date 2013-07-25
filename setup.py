from distutils.core import setup

setup(
    name='SkewT',
    version='0.1.3',
    author='Thomas Chubb',
    author_email='thomas.chubb@monash.edu',
    packages=['skewt'],
    scripts=[],
    url='http://pypi.python.org/pypi/SkewT/',
    license='LICENSE.txt',
    description='Plots and analyses atmospheric profile data',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)
