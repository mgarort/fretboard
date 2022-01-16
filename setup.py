import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fretboard',
    author='Miguel García Ortegón',
    description='A simple package to draw guitar a guitar fretboard and mark positions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mgarort/fretboard',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(where='fretboard.py'),
    python_requires='>=3.6',
)
