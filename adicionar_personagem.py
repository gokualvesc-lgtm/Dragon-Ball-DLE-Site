import sqlite3

conn = sqlite3.connect("PersonagensDB.db")
cursor = conn.cursor()

novos_personagens = [
    ("Mr. Satan", "Humano", "Bom", "Saga Cell", "Universo 7", "Guerreiros Z", "Terra", "Vivo"),
    ("Chi-Chi", "Humana", "Bom", "Saga Pilaf", "Universo 7", "Família Son", "Terra", "Vivo"),
    ("Ox-King", "Humano", "Bom", "Saga Pilaf", "Universo 7", "Montanha Frypan", "Terra", "Vivo"),
    ("Launch", "Humana", "Neutro", "Treinamento do Mestre Kame", "Universo 7", "Amigos do Mestre Kame", "Terra", "Vivo"),
    ("Yajirobe", "Humano", "Bom", "Saga Piccolo Daimaoh", "Universo 7", "Guerreiros Z", "Terra", "Vivo"),

    ("Kami Sama", "Namekuseijin", "Bom", "Saga Rei Demônio Piccolo", "Universo 7", "Guardiões da Terra", "Namekusei", "Morto"),
    ("Sr. Popo", "Ser Místico", "Bom", "Saga Rei Demônio Piccolo", "Universo 7", "Templo de Kami", "Desconhecido", "Vivo"),
    ("Rei Kaiô", "Kaiô", "Bom", "Saga Saiyajins", "Universo 7", "Deuses", "Outro Mundo", "Vivo"),
    ("Kaioshin", "Kaioshin", "Bom", "Saga Majin Boo", "Universo 7", "Deuses", "Mundo dos Kaioshins", "Vivo"),
    ("Kibito", "Kaioshin", "Bom", "Saga Majin Boo", "Universo 7", "Deuses", "Mundo dos Kaioshins", "Vivo"),

    ("Babidi", "Mago", "Mau", "Saga Majin Boo", "Universo 7", "Exército de Babidi", "Desconhecido", "Morto"),
    ("Dr. Gero", "Humano", "Mau", "Saga Androides", "Universo 7", "Exército Red Ribbon", "Terra", "Morto"),
    ("Android 19", "Androide", "Mau", "Saga Androides", "Universo 7", "Androides", "Terra", "Morto"),
    ("Android 20", "Androide", "Mau", "Saga Androides", "Universo 7", "Androides", "Terra", "Morto"),

    ("Tao Pai Pai", "Humano", "Mau", "Saga Red Ribbon", "Universo 7", "Assassinos", "Terra", "Vivo"),
    ("Comandante Red", "Humano", "Mau", "Saga Red Ribbon", "Universo 7", "Exército Red Ribbon", "Terra", "Morto"),
    ("General Blue", "Humano", "Mau", "Saga Red Ribbon", "Universo 7", "Exército Red Ribbon", "Terra", "Morto"),
    ("Mercenário Black", "Humano", "Mau", "Saga Red Ribbon", "Universo 7", "Exército Red Ribbon", "Terra", "Morto"),

    ("Rei Demônio Piccolo", "Namekuseijin", "Mau", "Saga Rei Demônio Piccolo", "Universo 7", "Demônios", "Namekusei", "Morto"),
    ("Tambourine", "Demônio", "Mau", "Saga Rei Demônio Piccolo", "Universo 7", "Demônios", "Terra", "Morto"),
    ("Drum", "Demônio", "Mau", "Saga Rei Demônio Piccolo", "Universo 7", "Demônios", "Terra", "Morto"),

    ("Broly", "Saiyajin", "Neutro", "Dragon Ball Super: Broly", "Universo 7", "Nenhum", "Planeta Vegeta", "Vivo"),
    ("Paragus", "Saiyajin", "Mau", "Dragon Ball Super: Broly", "Universo 7", "Nenhum", "Planeta Vegeta", "Morto"),
    ("Cheelai", "Alienígena", "Bom", "Dragon Ball Super: Broly", "Universo 7", "Força de Freeza", "Desconhecido", "Vivo"),
    ("Lemo", "Alienígena", "Bom", "Dragon Ball Super: Broly", "Universo 7", "Força de Freeza", "Desconhecido", "Vivo"),

    ("Frost", "Raça de Freeza", "Mau", "Torneio entre Universos 6 e 7", "Universo 6", "Nenhum", "Universo 6", "Vivo"),
    ("Magetta", "Metalman", "Bom", "Torneio entre Universos 6 e 7", "Universo 6", "Equipe Universo 6", "Universo 6", "Vivo"),
    ("Botamo", "Alienígena", "Bom", "Torneio entre Universos 6 e 7", "Universo 6", "Equipe Universo 6", "Universo 6", "Vivo"),

    ("Zamasu", "Kaioshin", "Mau", "Saga Goku Black", "Universo 10", "Deuses", "Universo 10", "Morto"),
    ("Goku Black", "Kaioshin", "Mau", "Saga Goku Black", "Universo 10", "Nenhum", "Universo 10", "Morto"),

    ("Dyspo", "Alienígena", "Bom", "Torneio do Poder", "Universo 11", "Tropa do Orgulho", "Universo 11", "Vivo"),
    ("Belmod", "Deus da Destruição", "Neutro", "Torneio do Poder", "Universo 11", "Deuses", "Universo 11", "Vivo"),
    ("Marcarita", "Anjo", "Neutro", "Torneio do Poder", "Universo 11", "Deuses", "Desconhecido", "Vivo")
]

cursor.executemany(
    """
    INSERT INTO personagens
    (nome, raca, alinhamento, saga, universo, grupo, planeta, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    novos_personagens
)

conn.commit()
conn.close()

print(f"{len(novos_personagens)} personagens adicionados com sucesso!")