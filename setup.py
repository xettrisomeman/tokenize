from setuptools import setup , find_packages

with open("README.md" , "r" , encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='nepalitokenizer',
    version='1.8.6.0',
    description = 'Tokenizes Nepali Text',
    py_modules=['nepalitokenizer'],
    package_dir={'':'src'},
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
    packages = find_packages(exclude='env'),
    include_package_data=True,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    extras_require={
        "dev":[
        "twine>=3.2.0",
        ]
    },
)

