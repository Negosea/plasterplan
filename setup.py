from setuptools import setup, find_packages

setup(
    name='plasterplan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  # Adicione outras dependências se houver
    ],
    author='Marcos sea',
    author_email='tecnosteelframe@gmail.com',
    description='Um pacote para cálculo de quantitativos de materiais para drywall.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/negosea/plasterplan',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    license='MIT',
)
