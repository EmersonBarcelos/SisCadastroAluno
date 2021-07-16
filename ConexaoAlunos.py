import mysql.connector
import os
try:
    con = mysql.connector.connect(host='localhost', database='db_alunos', user='litiane', password='')
except:
    print("Erro ao conectar ao banco de dados!")
def conectar():#Faz a conexão com o banco de dados
    cursor = con.cursor()
    db_info = con.get_server_info()
    print("Conectado ao servidor mysql versao",db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("conectado ao banco",linha)

def consultar():#Mostra todos os alunos cadastrados no banco de dados
    os.system("cls")
    cursor = con.cursor()
    consulta_sql = "select * from aluno_avaliacao"
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Numero total de alunos retornados: ", cursor.rowcount)

    print("\nMOSTRANDO OS ALUNOS CADASTRADOS\n")
    for linha in linhas:
        print("id:", linha[0])
        print("nome:", linha[1])
        print("nota 1:", linha[2])
        print("nota 2:", linha[3])
        print("turma:", linha[4])
        print("ano:", linha[5], "\n")

def inserir():#Solicita ao usuário os dados para inserção
    os.system("cls")
    cursor = con.cursor()
    id = input("Digite o ID:")
    nome = input("Digite o nome:")
    nota = input("Digite a nota:")
    turma = input("Digite a turma:")
    ano = input("Digite o ano:")
    cursor.execute(
        f"INSERT INTO aluno_avaliacao (id,nome,nota,turma,ano) VALUES ('{id}','{nome}','{nota}','{turma}','{ano}');")
    con.commit()
    print("==>ALUNO CADASTRADO COM SUCESSO<==")

def deletar():#Solicita o ID da linha em que deseja deletar todos os dados
    os.system("cls")
    cursor = con.cursor()
    id_aluno = input("Digite o ID do aluno que deseja deletar:")
    cursor.execute(f"DELETE FROM aluno_avaliacao WHERE id = '{id_aluno}';")
    con.commit()
    print("==>REGISTROS DELETADOS COM SUCESSO<==")

def total_notas():#Calcula a nota 1 com a nota 2 e mostra o total
    os.system("cls")
    cursor = con.cursor()
    id = input("DIGITE O ID DO ALUNO:")
    cursor.execute(f"select * from aluno_avaliacao where id = '{id}';")
    linhas = cursor.fetchone()
    resultado = linhas[2] + linhas[3]
    print("Nota total:", resultado)

def atualizar():#Solicita qual registro deseja atualizar
    os.system("cls")
    cursor = con.cursor()
    print("╔═══════════════════════╗")
    print("║[1]-NOME               ║")
    print("║[2]-NOTA 1             ║")
    print("║[3]-NOTA 2             ║")
    print("║[4]-TURMA              ║")
    print("╚═══════════════════════╝")
    op = input("Qual informação deseja atualizar?:")
    if (op == '1'):  # Atualiza o nome
        id = input("Digite o ID do registro:")
        nome = input("Qual o novo nome:")
        cursor.execute(f"UPDATE aluno_avaliacao SET nome = '{nome}' WHERE id = '{id}'")
        con.commit()
        print("-->REGISTRO ATUALIZADO<--")

    if (op == '2'):  # Atualiza a NOTA 1
        id = input("Digite o ID do registro:")
        nota1 = input("Qual a nova nota:")
        cursor.execute(f"UPDATE aluno_avaliacao SET nota1 = '{nota1}' WHERE id = '{id}'")
        con.commit()
        print("-->REGISTRO ATUALIZADO<--")

    if (op == '3'):  # Atualiza a NOTA 2
        id = input("Digite o ID do registro:")
        nota2 = input("Qual a nova nota:")
        cursor.execute(f"UPDATE aluno_avaliacao SET nota2 = '{nota2}' WHERE id = '{id}'")
        con.commit()
        print("-->REGISTRO ATUALIZADO<--")

    if (op == '4'):  # Atualiza a turma
        id = input("Digite o ID do registro:")
        turma = input("Qual a nova turma:")
        cursor.execute(f"UPDATE aluno_avaliacao SET turma = '{turma}' WHERE id = '{id}'")
        con.commit()
        print("-->REGISTRO ATUALIZADO<--")

if __name__=="__main__":
    conectar()
    print("\t\t| ** BEM VINDO AO BANCO DE DADOS ** |")
    def tela():
        print("╔═══════════════════════╗")
        print("║    MENU DE CADASTRO   ║")
        print("╠═══════════════════════╣")
        print("║[1]-CADASTRAR UM ALUNO ║")
        print("║[2]-DELETAR REGISTROS  ║")
        print("║[3]-LISTA DE ALUNOS    ║")
        print("║[4]-TOTAL DAS NOTAS    ║")
        print("║[5]-ATUALIZAR REGISTROS║")
        print("║[6]-SAIR               ║")
        print("╚═══════════════════════╝")
        opcao = input("-->")
        if opcao =='1':
            inserir()
        elif opcao =='2':
            deletar()
        elif opcao =='3':
            consultar()
        elif opcao =='4':
            total_notas()
        elif opcao =='5':
            atualizar()
        elif opcao =='6':
            pass
        else:
             os.system("cls")
             print("Essa opção não existe!")
             tela()
        retorno = input("DESEJA SAIR? (S)SIM (N)NÃO:")
        if (retorno.upper()=='N'):
            os.system("cls")
            tela()

tela()

if con.is_connected():
    cursor = con.cursor()
    cursor.close()
    con.close()
    print("Conexão encerrada")



    
