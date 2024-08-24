class Artista:
    def __init__(self, nome, genero):
        self.nome = nome
        self.genero = genero 
        self.albuns = [] #Lista para armazenar os álbuns do artista
    
    def __str__(self):
        return f'Nome: {self.nome} | Gênero Musical: {self.genero}'
    
    def adicionar_albuns(self,album):
        self.albuns.append(album)

    def visualizar_albuns(self):
        #Listar Albuns
        for albuns in self.albuns:
            print(albuns)

    @classmethod
    def criar_artista(cls, nome, genero):
        return cls(nome, genero)
    

class Album:
    def __init__(self, titulo, artista, ano_lancamento ):
        self.titulo = titulo
        self.artista = artista #Referencia ao objeto artista
        self.ano_lancamento = ano_lancamento
        self.musica = [] #Lista para armazenar as mucisa do album
    
    def __str__(self):
        return f'Título: {self.titulo} | Artista: {self.artista.nome} | Ano Lançamento: {self.ano_lancamento}'
    
    def adicionar_musica(self,musica):
        self.musica.append(musica)
    
    def visualizar_musica(self):
        for musica in self.musica:
            print(musica)

    
    @classmethod
    def criar_album(cls, titulo, artista, ano_lancamento):
     album = cls(titulo, artista, ano_lancamento)
     artista.adicionar_albuns(album)  # Use a instância 'artista'
     return album

class Musica:
    def __init__(self,titulo, duracao, artista, album):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista #Referencia ao objeto artista
        self.albuns = album #Referencia ao objeto album

    def __str__(self):
        return f'{self.titulo} | {self.duracao}min | {self.artista.nome} '
    
    def visualizar_albuns(self):
        #Listar Albuns
        for albuns in self.albuns:
            print(albuns)
            
    @property
    def descricao(self):
        return f'Música: {self.titulo} | Duração: {self.duracao} minutos | Artista: {self.artista.nome} | álbum: {self.albuns.titulo}'

 
#Exemplo:
#Criando um artista
print('Criando um Artista: ')
davidGuetta = Artista.criar_artista('David Guetta', 'Dance/Eletrônica')
print(davidGuetta)

#Criando um álbum e associando ao artista
print('\nCriando um álbum e associando ao artista: ')
listen = Album.criar_album('Listen', davidGuetta, '2014')
print(listen)

#criando música e associando ao álbum e ao artista
musica1 = Musica('Dangerous', 3.23, davidGuetta, listen)
musica2 = Musica ('What I did for love', 3.27, davidGuetta, listen)
musica3 = Musica ('No Momey no Love', 3.57, davidGuetta, listen)

#adicionando as músicas ao album
listen.adicionar_musica(musica1)
listen.adicionar_musica(musica2)
listen.adicionar_musica(musica3)

#visualizando as músicas do album
print('\nVisualizando as músicas do album:')
listen.visualizar_musica()

#Visualizando descrição detalhada de música
print('\nVisualizando descrição detalhada de música:')
print(musica1.descricao)
print(musica2.descricao)
print(musica3.descricao)



