from setuptools import setup, find_packages

setup(
    name='q3avant',
    version='0.2.0',
    author='Jordy Veenstra / A Pixelated Point of View',
    author_email='jordy.gaptx@gmail.com',
    description='Random data-generating algorithm for experimental Quake III Arena Machinima (post-)production',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jiyorude/avant',
    project_urls={
        "GitHub": "https://www.github.com/jiyorude/avant",
        "BitBucket": "https://bitbucket.org/appov/avant/src/main/",
        "Documentation": "https://avant-docs.vercel.app/",
        "Issues": "https://github.com/jiyorude/avant/issues",
        "PyPi": "#"
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        "inquirer>=3.2.3",
        "pymongo>=4.6.1",
        "reportlab>=4.0.9"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'q3avant_run = avant.avant:exec',
        ],
    },
)
