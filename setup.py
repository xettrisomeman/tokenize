from setuptools import setup

with open("README.md" , "r" , encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='nepalitokenizer',
    version='1.8.1.5',
    description = 'Tokenizes Nepali Text',
    py_modules=['nepalitokenizer'], 
    package_dir ={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ],
    package_data={'datafile':['STOP_WORDS.txt',]},
    long_description = long_description,
    long_description_content_type = "text/markdown",
    extras_require={
        "dev":[
        "twine>=3.2.0",
        ]
    },
)

