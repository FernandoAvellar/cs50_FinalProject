from cs50 import SQL

# Definindo as sessões da missa
SESSOES_DA_MISSA = {
    1:  "Entrada",
    2:  "Ato Penitencia",
    3:  "Glória",
    4:  "Salmo",
    5:  "Sequência",
    6:  "Aleluia",
    7:  "Ofertório",
    8:  "Santo",
    9:  "Consagração",
    10:  "Amém",
    11: "Paz",
    12: "Cordeiro",
    13: "Comunhão",
	14: "Saída",
	15: "Diversas"
}

db = SQL("sqlite:///database/database.db")

def main():

    while True:
        print("\n##########################################")
        print(f"Organizador de Cifras")
        print("##########################################")
        print("1 - Inserir nova cifra")
        print("2 - Visualizar todas as cifras")
        print("3 - Visualizar cifras por sessão da missa")
        print("4 - Selecionar cifras para a próxima missa")
        print("5 - Sair")
        print("###########################################")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_cifra()
        elif opcao == '2':
            visualizar_todas_cifras()
        elif opcao == '3':
            visualizar_cifras_por_sessao()
        elif opcao == '4':
            selecionar_cifras_para_missa()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")


def inserir_cifra():
    nome_musica = input("Digite o nome da música: ")
    # Solicitando a sessão e validando se é uma sessão válida
    for num, sessao in sorted(SESSOES_DA_MISSA.items()):
        print(f"{num} - {sessao}")

    while True:
        sessao = input("Escolha o número da sessão dessa música: ")

        # Verifica se a entrada é numérica
        if not sessao.isdigit():
            print("Por favor, digite apenas números.")
            continue

        sessao = int(sessao)

        # Verifica se a entrada está dentro do intervalo das sessões da missa
        if sessao not in SESSOES_DA_MISSA:
            print("Sessão inválida. Por favor, escolha uma sessão válida.")
            continue

        # Convertendo o numero escohido para o nome da sessão que será salvo no arquivo
        sessao = SESSOES_DA_MISSA[sessao] 
    
        print("Digite a cifra da música (digite 'FINAL' em uma linha separada para indicar o final da cifra):")
        cifra = ""
        while True:
            linha = input()
            if linha.strip() == "FINAL":
                break
            cifra += linha + "\n"

        cifra = cifra.strip()
        db.execute("INSERT INTO cifras (nome, sessao, cifra) VALUES(?, ?, ?)", nome_musica, sessao, cifra)
        return



def visualizar_cifras_por_sessao():
    print("Sessões da missa:")
    for num, sessao in sorted(SESSOES_DA_MISSA.items()):
        print(f"{num} - {sessao}")

    while True:
        sessao_num = input("Escolha o número da sessão que deseja visualizar: ")

        # Verifica se a entrada é numérica
        if not sessao_num.isdigit():
            print("Por favor, digite apenas números.")
            continue

        sessao_num = int(sessao_num)

        # Verifica se a entrada está dentro do intervalo das sessões da missa
        if sessao_num not in SESSOES_DA_MISSA:
            print("Sessão inválida. Por favor, escolha uma sessão válida.")
            continue

        sessao = SESSOES_DA_MISSA[sessao_num]
        print(f"\nCifras da sessão '{sessao}':")
        print("-------------")
        print(" Num  |  Nome")
        print("-------------")
        cifras = db.execute("SELECT * FROM cifras WHERE sessao = ?", sessao)
        for cifra in cifras:
            print(f"| {cifra['id']} |  {cifra['nome']}")
        break



def visualizar_todas_cifras():
    print(f"\nCifras salvas:")
    print("-------------")
    print(" Num  |  Nome")
    print("-------------")
    cifras = db.execute("SELECT * FROM cifras")
    for cifra in cifras:
        print(f"| {cifra['id']} |  {cifra['nome']} ({cifra['sessao']})")



def selecionar_cifras_para_missa():
    cifras_selecionadas = input("Digite os números das cifras que serão usadas na próximo missa (separados por vírgula): ")
    
    # Verifica se a entrada está vazia
    if not cifras_selecionadas.strip():
        print("Nenhum número de cifra foi fornecido.")
        return
    
    selecionadas = cifras_selecionadas.split(',')
    selecionadas_validas = []

    with open("cifras_selecionadas.txt", "w") as f:
        for selecionada in selecionadas:
            selecionada = int(selecionada.strip())
            cifra = db.execute("SELECT * FROM cifras WHERE id = ?", selecionada)
            if len(cifra) != 0:
                f.write(f"{cifra[0]['sessao']}\n\nMúsica: {cifra[0]['nome']}\n\n{cifra[0]['cifra']}\n\n")
                selecionadas_validas.append(cifra[0]['nome'])
            else:
                print(f"Cifra de número {selecionada} não encontrada.")

    if selecionadas_validas:
        print("As seguintes cifras foram selecionadas com sucesso:")
        for cifra_nome in selecionadas_validas:
            print(cifra_nome)

    return


if __name__ == "__main__":
    main()