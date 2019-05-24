# Tutorial de flask e flask_restplus
## Descrição
Este repositório tem como objetivo somente **exemplificar o funcionamento e desenvolvimento de uma aplicação Python com flask e flask_restplus**, assim como publicar em um servidor Nginx com UWSGI em um servidor Ubuntu 18.04 LTS.

## Requisitos
### Desenvolvimento
- [**Python 3**](https://www.python.org/downloads/)

### Publicação
- [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/)

## Conteudo
- [Ambiente virtual](#ambientevirtual)
- [Organização do projeto](#organizacaodoprojeto)
- [Classes](#classes)
- [Doc Strings](#docstrings)
- [UWSGI](#uwsgi)
- [Nginx](#nginx)

## Desenvolvimento
### <a name="ambientevirtual">Ambiente virtual</a>
Sempre que iniciar um projeto colaborativo é recomendado criar um ambiente virtual para que outros desenvolvedores possam replicar e manter a coerência do projeto.

#### Windows
Para criar um ambiente virtual em Windows utiliza os seguintes passos:
- instalar o pacote virtualenv:
```cmd
> pip install virtualenv
```
- criar o ambiente virtual:
```cmd
> python -m virtualenv virtualenv
```
- ativar o ambiente virtual:
```cmd
> .\virtualenv\Scripts\activate
```

#### Linux
Para criar um ambiente virtual em Linux utiliza os seguintes passos:
- instalar o pacote venv:
```bash
$ apt-get install python3-dev python3-venv
$ pip install virtualenv
```
- criar o ambiente virtual:
```bash
$ python -m venv virtualenv
```
- ativar o ambiente virtual:
```bash
$ source virtualenv/bin/activate
```

#### Mac
Para criar um ambiente virtual em Mac sutiliza os seguintes passos:
- instalar o pacote virtualenv:
```bash
$ pip install virtualenv
```
- criar o ambiente virtual:
```bash
$ python -m virtualenv virtualenv
```
- ativar o ambiente virtual:
```bash
$ source virtualenv/bin/activate
```

### Sair do ambiente
em todos os casos para sair do ambiente basta enviar o comando `deactivate`.

### <a name="organizacaodepastas">Organização do projeto</a>
No projeto o `app.py` é responsável pela aplicação principal, na pasta `apis` ficam os namespaces da api, o `core` é responsável por ter as regras de negócios assim como os modelos de objetos, `utils` tem somente módulos que auxiliam a aplicação porém não parte integrantes, o `requirements.txt` contém a lista de dependências de módulos do projeto.
```
.
|-- LICENSE
|-- README.md
|-- apis
|   `-- exemplo.py
|-- app.py
|-- core
|   `-- exemplo_controlador.py
|-- requirements.txt
`-- utils
    `-- exemplo_utilitario.py
```
### <a name="classes">Classes</a>
As classes tem o mesmo princípio de outras linguagens orientadas a objeto porém um módulo pode conter mais de uma classe conforme sua afinidade, seu método construtor é caracterizado pela função `__init__`
- Classe 

- Herança
```python
class Animal():
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f'O {self.__nome} está comendo.')
```
```python
import animal

class Cachorro(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def latir(self):
        print('Au au.')


class Gato(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    
    def miar(self):
        print('Miau.')
```

- Polimorfismo
```python
class Forma_geometrica:
def calcular_area(self):
    pass
```
```python
class Retangulo(Forma_geometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calc_area(self):
        return self.base * self.altura


class Circulo(Forma_geometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calc_area(self):
        return self.raio * self.raio * 3.14
```

### <a name="docstrings">Doc Strings</a>
Deentre os modelos de documentação

## Publicação
#TODO

## Referências e links úteis:
- [Python](https://docs.python.org/3/)
- [Udacity](https://www.udacity.com/course/introduction-to-python--ud1110)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)
- [Flask](http://flask.pocoo.org/)
- [flask_restplus](https://flask-restplus.readthedocs.io/en/stable/)
- [Requests](https://2.python-requests.org/en/master/)

## Autor
- **Paulo Henrique** - [PH](https://github.com/paulo-henrique-ph)