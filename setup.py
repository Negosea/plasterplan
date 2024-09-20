from setuptools import setup, find_packages

setup(
    name='plasterplan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',  # Adicione outras dependências se houver
    ],
    author='Marcos sea',  # Substitua pelo seu nome
    author_email='tecnosteelframe@gmail.com',  # Substitua pelo seu e-mail
    description='Um pacote para cálculo de quantitativos de materiais para drywall.',
    url='https://github.com/negosea/plasterplan',  # Substitua pela URL do seu repositório
)
