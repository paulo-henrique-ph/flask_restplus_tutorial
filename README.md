# Tutorial de flask e flask_restplus
## Descrição
Este repositório tem como objetivo somente **exemplificar o funcionamento e desenvolvimento de uma aplicação Python com flask e flask_restplus**, assim como publicar em um servidor Nginx com uWSGI em um servidor Ubuntu 18.04 LTS.

## Requisitos
### Desenvolvimento
- [**Python 3**](https://www.python.org/downloads/)

### Publicação
- [Ubuntu 18.04 LTS](http://releases.ubuntu.com/18.04/)

## Conteúdo
- [Ambiente virtual](#ambientevirtual)
- [Organização do projeto](#organizacaodoprojeto)
- [Classes](#classes)
- [Doc Strings](#docstrings)
- [uWSGI](#uwsgi)
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
$ apt install python3-dev python3-venv
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
```python
class ClasseExemplo:
    def __init__(self):
        self.url = 'https://api.ipify.org'
    
    def consulta_com_nome(self):
        util = Utilitario()
        util.ser_util()
        try:
            response = requests.get(self.url)
            return json.loads(response.content), True
        except:
            return 'Não conseguimos nos conectar', False
```

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
class FormaGeometrica:
def calcular_area(self):
    pass
```
```python
class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calc_area(self):
        return self.base * self.altura


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calc_area(self):
        return self.raio * self.raio * 3.14
```

### <a name="docstrings">Doc Strings</a>
Dentre os modelos de documentação um dos mais utilizados é o padraão da Google

## Publicação
### <a name="uwsgi">uWSGI</a>
#### Pré requisitos da máquina
Após ter seu projeto inserido na máquina precisa-se de alguns passos antes de implementar a aplicação.

- Instalar os pacotes de virtual enviroment
```
$ sudo apt update
$ sudo apt install python-pip
$ pip install virtualenv
$ sudo apt install python3-venv
$ sudo apt install python3-dev
```
- Criar o diretório da aplicação
```bash
$ mkdir -p /var/www/html/exemplo
```

- Mover os arquivos para seus devidos lugares
Todos os arquivos referentes a aplicação assim como `exemplo.ini` deverão ficar no diretório `/var/www/html/exemplo`

- Criar enviroment
```bash
$ cd /var/www/html/exemplo
$ python3 -m venv virtualenv
```

- Ativar o enviroment e instalar as dependências
```bash
$ source virtualenv/bin/activate
$ pip install wheel
$ pip install uwsgi
$ pip install -r requirements.txt
$ deactivate
```

- Ativar o serviço
após copiar o `exemplo.service` para o diretório `/etc/systemd/system` precisará mudar algumas autorizações no qual será necessário [**Root**](https://help.ubuntu.com/community/RootSudo)

```bash
$ chown -R www-data:www-data /var/www/html/exemplo
$ systemctl daemon-reload
$ systemctl start exemplo
$ systemctl enable exemplo
```

### <a name="nginx">Nginx</a>
#### Instalando e configurando o Nginx
Para instalar e configurar o Nginx  a fim de disponibilzar sua aplicação ao público precisa seguir os seguintes passos

- Instalar o Nginx
```bash
$ apt install nginx
```

- Remover o site default do nginx
```bash
$ rm /etc/nginx/sites-available/default
$ rm /etc/nginx/sites-enabled/default
$ sudo ufw 'Nginx Full'
$ sudo systemctl restart nginx
```
- Editar o arquivo de configuração do Nginx
```bash
$ sudo vim /etc/nginx/nginx.conf
```

Adicionar logo abaixo do "http {"
```
client_max_body_size 16M;
```

Reiniciar o serviço
```bash
$ sudo systemctl restart nginx
```

- Ativar o site
Após copiar o `exemplo.conf` para o diretório `/etc/nginx/sites-available` executar os seguintes comandos
```bash
$ ln -s /etc/nginx/sites-available/exemplo.conf /etc/nginx/sites-enabled/exemplo.conf
$ sudo systemctl reload nginx
```

## Referências e links úteis:
- [Flask](http://flask.pocoo.org/)
- [flask_restplus](https://flask-restplus.readthedocs.io/en/stable/)
- [Google Doc String](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- [Python](https://docs.python.org/3/)
- [PEP8](https://www.python.org/dev/peps/pep-0008/)
- [Requests](https://2.python-requests.org/en/master/)
- [Udacity Python Fundamentals](https://www.udacity.com/course/introduction-to-python--ud1110)
- [Udacity - Git Version Control](https://www.udacity.com/course/version-control-with-git--ud123)
- [Udacity - Github & Collaboration](https://www.udacity.com/course/github-collaboration--ud456)

## Autor
- **Paulo Henrique** - [PH](https://github.com/paulo-henrique-ph)