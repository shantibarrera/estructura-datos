# SE IMPORTAN LAS BIBLIOTECAS A USAR
import networkx as nx # NOS AYUDA CON LA VISUALIZACION DEL GRAFO
import matplotlib.pyplot as plt # NOS AYUDA CON LA RELACION ENTRE LOS DATOS DEL GRAFO Y SU CREACION
import random # NOS AYUDA A GENERAR NUMEROS ALEATORIOS (RANKIN DE PELICULAS)



G = nx.Graph()


users = ["Santiago", "Melissa", "Kerly", "Cristian", "Emanuel"]
G.add_nodes_from(users)


# COMENTAR SI SE QUIERE VER SOLO LA RELACIÓN PERSONA-PELICULA Y NO PERSONA-PELICULA-PERSONA
#friendships = [("Santiago", "Melissa"), ("Santiago", "Kerly"), ("Santiago", "Cristian"), ("Santiago", "Emanuel"),
#               ("Melissa", "Kerly")]
#G.add_edges_from(friendships)


mc5 = []
mc4 = []
mc3 = []
mc2 = []
mc1 = []



movie_names = ["Maze Runner", "John Wick", "Fast and Furious", "Duro de Matar", "El Justiciero",
                "Titanes del Pacifico", "Misión Imposible", "King's Man", "Avengers", "Tren Bala",
                "Don Nadie", "XXX", "Top Gun", "Los Juegos del Hambre", "Matrix", "Batman",
                "Mad Max", "Free Guy", "Dunkirk", "Divergente"]
movie_ratings = {}
for user in users:
    movies_watched = random.sample(movie_names, 5)
    ratings = [random.randint(1, 5) for _ in range(5)]
    user_ratings = dict(zip(movies_watched, ratings))
    movie_ratings[user] = user_ratings

    for movie, rating in zip(movies_watched, ratings):
        G.add_node(user)
        G.add_node(movie)
        G.add_edge(user, movie, rating=rating)


mc5_connections = []

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 5:
            mc5_connections.append(("mc5", movie))

G.add_node("mc5")
G.add_edges_from(mc5_connections)



mc4_connections = []

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 4:
         
            mc4_connections.append(("mc4", movie))

G.add_node("mc4")
G.add_edges_from(mc4_connections)


mc3_connections = []

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 3:
        
            mc3_connections.append(("mc3", movie))

G.add_node("mc3")
G.add_edges_from(mc3_connections)



mc2_connections = []

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 2:
   
            mc2_connections.append(("mc2", movie))

G.add_node("mc2")
G.add_edges_from(mc2_connections)


mc1_connections = []

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 1:
          
            mc1_connections.append(("mc1", movie))

G.add_node("mc1")
G.add_edges_from(mc1_connections)



mc5 = {user: {movie: rating for movie, rating in user_ratings.items() if rating == 5} for user, user_ratings in movie_ratings.items()}
mc4 = {user: {movie: rating for movie, rating in user_ratings.items() if rating == 4} for user, user_ratings in movie_ratings.items()}
mc3 = {user: {movie: rating for movie, rating in user_ratings.items() if rating == 3} for user, user_ratings in movie_ratings.items()}
mc2 = {user: {movie: rating for movie, rating in user_ratings.items() if rating == 2} for user, user_ratings in movie_ratings.items()}
mc1 = {user: {movie: rating for movie, rating in user_ratings.items() if rating == 1} for user, user_ratings in movie_ratings.items()}


pos = nx.spring_layout(G)



nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, edge_color='gray')



print(" ")
print(" ")
print("Bienvenido. Las peliculas mostradas son valoradas por el usuario y todas se valoran sobre 5 puntos. Siendo 1 muy mala y 5 muy buena.")
print(" ")
print(" ")
print("------------- PELICULAS VISTAS POR USUARIOS -------------")
print(" ")
for user, ratings in movie_ratings.items():
    print(f"El usuario {user} valoró las peliculas con un ranking: {ratings}")
    print(" ")


# SE IMPRIMEN LAS LISTAS DE PELICULAS VALORADAS DEL 1 AL 5
print(" ")
print("------------- PELICULAS VALORADAS EN 5 POR USUARIOS -------------")
print(" ")
print("Peliculas 5/5: ", mc5)
print(" ")
print("------------- PELICULAS VALORADAS EN 4 POR USUARIOS -------------")
print(" ")
print("Peliculas 4/5: ", mc4)
print(" ")
print("------------- PELICULAS VALORADAS EN 3 POR USUARIOS -------------")
print(" ")
print("Peliculas 3/5: ", mc3)
print(" ")
print("------------- PELICULAS VALORADAS EN 2 POR USUARIOS -------------")
print(" ")
print("Peliculas 2/5: ", mc2)
print(" ")
print("------------- PELICULAS VALORADAS EN 1 POR USUARIOS -------------")
print(" ")
print("Peliculas 1/5: ", mc1)


# RECOMENDADOR DE PELICULAS
print(" ")
print(" ------------------------------------------------ ")
print(" ")
print("------------- PELICULAS RECOMENDADAS -------------")
print(" ")

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 5:
            print(f"{user} te recomienda {movie} valorada en {5} estrellas")
            print(" ")


for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 4:
            print(f"{user} te recomienda {movie} valorada en {4} estrellas")
            print(" ")


for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 3:
            print(f"{user} te recomienda {movie} valorada en {3} estrellas")
            print(" ")

print(" --------------------------------------------------- ")
print(" ")
print("------------- PELICULAS NO RECOMENDADAS -------------")
print(" ")

for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 2:
            print(f"{user} NO te recomienda {movie} valorada en {2} estrellas")
            print(" ")


for user, ratings in movie_ratings.items():
    for movie, rating in ratings.items():
        if rating == 1:
            print(f"{user} NO te recomienda {movie} valorada en {1} estrellas")
            print(" ")


# SE IMPRIME EL GRAFO EN VENTANA EMERGENTE
plt.title("Recomendador de Peliculas")
plt.show()