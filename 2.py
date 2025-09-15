#Phelipe
#30. Controle de compras pessoais
#Pedidos: Add itens, preço, remoção, quantidade, preço final, editar e um menu.
from colorama import Fore, Style, init
from pyfiglet import Figlet
from rich.table import Table
from rich.console import Console


init(autoreset=True)
console = Console()

compras = []

def titulo():
    f = Figlet(font="slant")
    print(Fore.CYAN + f.renderText("Controle de Compras") + Style.RESET_ALL)

def adicionar_compra():
    produto = input(Fore.CYAN + "Digite o nome do produto: " + Style.RESET_ALL)
    preco = float(input(Fore.CYAN + "Digite o preço do produto: " + Style.RESET_ALL))
    quantidade = int(input(Fore.CYAN + "Digite a quantidade: " + Style.RESET_ALL))
    compras.append({"produto": produto, "preco": preco, "quantidade": quantidade})
    print(Fore.GREEN + "✔ Compra adicionada com sucesso!\n")

def remover_compra():
    listar_compras()
    if compras:
        indice = int(input(Fore.CYAN + "Digite o número da compra que deseja remover: " + Style.RESET_ALL)) - 1
        if 0 <= indice < len(compras):
            compras.pop(indice)
            print(Fore.GREEN + "✔ Compra removida com sucesso!\n")
        else:
            print(Fore.RED + "✘ Número inválido!\n")

def editar_compra():
    listar_compras()
    if compras:
        indice = int(input(Fore.CYAN + "Digite o número da compra que deseja editar: " + Style.RESET_ALL)) - 1
        if 0 <= indice < len(compras):
            produto = input(Fore.CYAN + "Novo nome do produto: " + Style.RESET_ALL)
            preco = float(input(Fore.CYAN + "Novo preço: " + Style.RESET_ALL))
            quantidade = int(input(Fore.CYAN + "Nova quantidade: " + Style.RESET_ALL))
            compras[indice] = {"produto": produto, "preco": preco, "quantidade": quantidade}
            print(Fore.GREEN + "✔ Compra editada com sucesso!\n")
        else:
            print(Fore.RED + "✘ Número inválido!\n")

def listar_compras():
    if not compras:
        print(Fore.RED + "✘ Nenhuma compra cadastrada.\n")
    else:
        table = Table(title="Lista de Compras", show_lines=True)
        table.add_column("Nº", justify="center", style="cyan", no_wrap=True)
        table.add_column("Produto", style="yellow")
        table.add_column("Preço (R$)", justify="right", style="green")
        table.add_column("Qtd", justify="center", style="magenta")
        table.add_column("Subtotal (R$)", justify="right", style="red")

        total = 0
        for i, compra in enumerate(compras, start=1):
            subtotal = compra["preco"] * compra["quantidade"]
            total += subtotal
            table.add_row(
                str(i),
                compra["produto"],
                f"{compra['preco']:.2f}",
                str(compra["quantidade"]),
                f"{subtotal:.2f}"
            )

        console.print(table)
        console.print(Fore.MAGENTA + f"\nTotal da compra: R${total:.2f}\n")

def menu():
    while True:
        titulo()
        print(Fore.BLUE + "==== Menu Principal ====" + Style.RESET_ALL)
        print(Fore.YELLOW + "1 - Adicionar compra")
        print("2 - Remover compra")
        print("3 - Editar compra")
        print("4 - Ver compras")
        print("0 - Sair" + Style.RESET_ALL)
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            adicionar_compra()
        elif opcao == "2":
            remover_compra()
        elif opcao == "3":
            editar_compra()
        elif opcao == "4":
            listar_compras()
        elif opcao == "0":
            print(Fore.GREEN + "✔ Saindo... Obrigado por usar o sistema!")
            break
        else:
            print(Fore.RED + "✘ Opção inválida!\n")

menu()