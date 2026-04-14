# Criação da classe de cadastro de jogadores
class cadastro_jogador:
    def __init__(self, nome, nickName, turma):
        self.nome = nome
        self.nickName = nickName
        self.turma = turma

# Criação da classe de cadastro de equipe
class cadastro_equipe:
    def __init__(self, nome_equipe, jogo_escolhido):
        self.nome_equipe = nome_equipe
        self.jogo_escolhido = jogo_escolhido       
        self.lista_jogadores = []  # lista que guarda jogadores

# lista para guardar 3 equipes do campeonato
campionato_equipes = []

# loop para tres equipes
for i in range(3):
    print(f"\nCadastro da equipe {i + 1}")
    nome_e = input("Nome da equipe: ")
    jogo_e = input(" escolha os Jogo disputados valorant, lol, ou rl : ")

    # criação do objeto da equipe atual
    equipe_atual = cadastro_equipe(nome_e, jogo_e)

    # loop para os 10 jogadores dessa equipe específica
    print(f"\nCadastro de 10 jogadores para a equipe {nome_e}")
    for j in range(10):
        print(f"Jogador {j+1}/10:")
        n = input("Nome: ")
        nk = input("Nickname: ")
        t = input("Turma: ")

        # criação do objeto jogador e adiciona na equipe
        novo_jogador = cadastro_jogador(n, nk, t)
        equipe_atual.lista_jogadores.append(novo_jogador)

    #  LINHAS 42 E 43 
    campionato_equipes.append(equipe_atual)
    print("\nCadastro concluído com sucesso!")
