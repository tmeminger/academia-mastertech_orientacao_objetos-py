# def numeros (7, 4, 13):
# print numeros 

# def lista_de_filmes(pessoa, *args):
#     print(f'Lista de Filmes Favoritos de {pessoa}:')
#     for item in args:
#         print(item)

# lista_de_filmes('Camila', 'Shutter Island', 'Submarine', 'Interstellar', 'Paths of Glory')
# lista_de_filmes('Thales', 'Be Kind Rewind', 'Spider-Man Homecoming')
# lista_de_filmes('Italo', 'Nenhum filme favoritado')

def lista_de_filmes(**kwargs):
    titulo = kwargs.get('suspense')
    if titulo is not None:
        print(f'Na lista há um titulo: {titulo}')

lista_de_filmes(suspense=['Shutter Island', 'Agora', 'A Clockwork Orange'], aventura='Spider-Man Homecoming', indie='Submarine')
lista_de_filmes(metalinguagem='Be Kind Rewind', guerra='Paths of Glory', scifi='Interstellar')