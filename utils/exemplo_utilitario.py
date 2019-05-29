class Utilitario:
    def __init__(self):
        '''Classe utilitária
        '''
        self.__propriedade = 'Sou muito útil.'  # atributos internos
        # (private em outras linguagens)
        # começam com 2 underscores

    def ser_util(self):
        '''Método da classe utilitária

        `Returns`: proprieade
        '''
        print(self.__propriedade)
