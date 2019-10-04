import sqlite3
import datetime
import pandas as pd

class menu():
    def __init__(self):
        self.contin = True
    def principal(self):
        print('0 - Sair\n1 - Clientes\n2 - Contas\n3 - Historico')
        op = int(input('Digite a opção:. '))
        if op == 0:
            self.contin = False
        elif op == 1:
            self.menuClientes()
        elif op == 2:
            self.menuContas()
        elif op == 3:
            self.menuHistorico()
        else:
            print('Opção Inválida')
    def menuClientes(self):
        print('1 - Criar cliente \n2 - Pesquisar Cliente \n3 - Atualizar Cliente \n4 - Remover Cliente\n5 - Dados da Tabela')
        print("Insira a opção abaixo:. ")
        op = int(input('Opção:. '))
        if op==1:
            admin.insert(input('Nome:. '),input('CPF:. '),input('Sexo:. '))
        elif op == 2:
            admin.search(int(input('INDEX:. ')))
        elif op == 3:
            admin.atualizarCliente(int(input('INDEX:. ')))
        elif op == 4:
            print(admin.get_Dados())
            admin.remove(int(input('INDEX:. ')))
        elif op == 5:
            print(admin.get_Dados())
        elif op == 0:
            self.principal()
        else:
            print('Opção Inválida')
    def menuContas(self):
        print('0 - Voltar\n1 - Criar\n2 - Extrato\n3 - Depositar\n4 - Sacar\n5 - Transferência\n6 - Remover\n7 - Dados da Tabela')
        op = int(input('Digite a opção:. '))
        if op == 0:
            self.principal()
        elif op == 1:
            admin.get_Dados()
            contas.adicionar(input('Número da Conta'),admin.df._get_value(int(input('INDEX Cliente:. ')),'nome'),input('Número do Historico'))
        elif op == 2:
            contas.extrato(int(input('IDEX:. ')))
        elif op == 3:
            contas.deposita(int(input('INDEX:. ')))
        elif op == 4:
            contas.sacar(int(input('INDEX:. ')))
        elif op == 5:
            contas.transferir(int(input('INDEX:. ')),int(input('INDEX Destino:. ')))
        elif op == 6:
            print(contas.get_Dados())
            contas.remove(int(input('INDEX:. ')))
        elif op == 7:
            print(contas.get_Dados())
        else:
            print('Opção Inválida')
    def menuHistorico(self):
        print('0 - Voltar\n 1 - Imprimir\n 2 - Dados da Tabela')
        op = int(input('Digite a opção:. '))
        if op == 0:
            self.principal()
        elif op == 1:
            historico.imprimir(contas.df._get_value(int(input('INDEX Conta:. ')), 'HistoricoID'))
        elif op == 2:
            print(historico.df)
        else:
            print('Opção Inválida')

class Clientes():
    def __init__(self):
        self.count = 0
    def init(self):
        self.conn = sqlite3.connect('dados.db')
        self.cursor = self.conn.cursor()
        try:
            self.df = pd.read_sql('SELECT * FROM Clientes', self.conn, 'index')
        except:
            self.create()
    def create(self):
        self.df = pd.DataFrame(None, None, ('nome', 'cpf', 'sexo'))
        self.df.to_sql('Clientes', self.conn,  None,  """replace""")
        self.disconnect()
    def search(self,index):
        self.init()
        try:
            lista = [self.df._get_value(int(index),'nome'),self.df._get_value(int(index),'cpf'),self.df._get_value(int(index),'sexo')]
            print(lista)
        except:
            print('Nenhuma Correspondencia!!')
        finally:
            self.disconnect()
    def insert(self, nome, cpf, sexo):
        self.init()
        self.df = self.df.append({'nome':nome, 'cpf':cpf, 'sexo':sexo},True)
        self.disconnect()
    def remove(self,index):
        self.init()
        try:
            self.df = self.df.drop([int(index)])
        except:
            print("Nenhuma Correspondencia!!")
        finally:
            self.atualizarLista()
    def atualizarLista(self):
        self.df = self.df.reset_index(drop=True)
        self.disconnect()
    def atualizarCliente(self,index):
        self.init()
        nome = input('Nome(pressione ENTER para não alterar):. ')
        if nome != '':
            self.df = self.df._set_value(index,'nome',nome)
        cpf = input('CPF(pressione ENTER para não alterar):. ')
        if cpf != '':
            self.df = self.df._set_value(index, 'cpf',cpf)
        sexo = input('Sexo(pressione ENTER para não alterar):. ')
        if sexo != '':
            self.df = self.df._set_value(index,'sexo',sexo)

    def get_Dados(self):
        return(self.df)
    def disconnect(self):
        self.df.to_sql('Clientes', self.conn, None, """replace""")
        self.cursor.close()
        self.conn.close()

class Conta():
    def __init__(self):
        pass
    def init(self):
        self.conn = sqlite3.connect('dados.db')
        self.cursor = self.conn.cursor()
        try:
            self.df = pd.read_sql('SELECT * FROM Contas', self.conn, 'index')
        except:
            self.create()
    def get_Dados(self):
        return(self.df)
    def extrato(self,index):
        print('Cliente: {}\nSaldo: {}\n'.format(self.df._get_value(index,'Cliente'),self.df._get_value(index,'Saldo')))
    def create(self):
        self.df = pd.DataFrame(None, None, ('Numero_da_Conta', 'Cliente', 'Saldo','Limite','HistoricoID'))
        self.df.to_sql('Contas', self.conn, None, """replace""")
        self.disconnect()
    def adicionar(self,nrConta,cliente,historico):
        self.init()
        self.df = self.df.append({'Numero_da_Conta': nrConta, 'Cliente': cliente, 'Saldo': 0.0, 'Limite': 0.0, 'HistoricoID': historico}, True)
        self.disconnect()
    def deposita(self,index):
        self.init()
        valor = float(input('Digite o valor para depositar:. '))
        self.df = self.df._set_value(index, 'Saldo', int(self.df._get_value(index, 'Saldo'))+valor)
        historico.adicionar(self.df._get_value(index, 'HistoricoID'),('Depositado R$ '+str(valor)))
        self.disconnect()
    def sacar(self,index):
        self.init()
        valor = float(input('Digite o valor para sacar:. '))
        if(int(self.df._get_value(index, 'Saldo'))-valor >= int(self.df._get_value(index, 'Limite'))):
            self.df = self.df._set_value(index, 'Saldo', int(self.df._get_value(index, 'Saldo'))-valor)
            historico.adicionar(self.df._get_value(index, 'HistoricoID'),('Sacado R$ '+str(valor)))
        else:
            print('Saldo Insuficiente!!')
        self.disconnect()
    def transferir(self,index,indexD):
        self.init()
        valor = float(input('Digite o valor para transferir:. '))
        try:
            if(int(self.df._get_value(index, 'Saldo'))-valor >= int(self.df._get_value(index, 'Limite'))):
                self.df = self.df._set_value(index, 'Saldo', int(self.df._get_value(index, 'Saldo'))-valor)
                self.df = self.df._set_value(indexD, 'Saldo', int(self.df._get_value(indexD, 'Saldo')) + valor)
                historico.adicionar(self.df._get_value(index, 'HistoricoID'),('Transferido R$ '+str(valor)+' para '+str(self.df._get_value(indexD, 'Cliente'))))
                historico.adicionar(self.df._get_value(indexD, 'HistoricoID'), ('Recebido via Transferência R$ ' + str(valor)))
                print('Transferido com Sucesso!!')
            else:
                print('Saldo Insuficiente!!')
        except:
            print('Ocorreu um Erro na Transferência!!')
        finally:
            self.disconnect()
    def remove(self,index):
        self.init()
        try:
            historico.remove(int(self.df._get_value(index)), 'HistoricoID')
            self.df = self.df.drop([int(index)])
        except:
            print("Nenhuma Correspondencia!!")
        finally:
            self.atualizarLista()
    def atualizarLista(self):
        self.df = self.df.reset_index(drop=True)
        self.disconnect()
    def disconnect(self):
        self.df.to_sql('Contas', self.conn, None, """replace""")
        self.cursor.close()
        self.conn.close()

class Historico():
    def __init__(self):
        pass

    def init(self):
        self.conn = sqlite3.connect('dados.db')
        self.cursor = self.conn.cursor()
        try:
            self.df = pd.read_sql('SELECT * FROM Historico', self.conn, 'index')
        except:
            self.create()

    def create(self):
        self.df = pd.DataFrame(None, None, ('HistoricoID', 'Evento','Data_de_Abertura'))
        self.df.to_sql('Historico', self.conn, None, """replace""")
        self.disconnect()
    def adicionar(self,id,msg):
        self.init()
        data_atual = datetime.datetime.today()
        data = '{}-{}-{} {}:{}:{}'.format(data_atual.day, data_atual.month, data_atual.year, data_atual.hour,
                                          data_atual.minute, data_atual.second)
        self.df = self.df.append(
            {'HistoricoID': id, 'Evento': msg, 'Data_de_Abertura': str(data)},
            True)
        self.disconnect()
    def imprimir(self,id):
        self.init()
        self.cursor.execute("""SELECT * FROM Historico WHERE HistoricoID=?""",(id,))
        for linha in self.cursor.fetchall():
            print(linha)
    def remove(self,id):
        self.init()
        try:
            self.cursor.execute("""SELECT * FROM Historico WHERE HistoricoID=?""", (id,))
            for linha in self.cursor.fetchall():
                self.df = self.df.drop([int(linha[0])])
        except:
            print("Nenhuma Correspondencia!!")
        finally:
            self.disconnect()
    def disconnect(self):
        self.df.to_sql('Historico', self.conn, None, """replace""")
        self.cursor.close()
        self.conn.close()

admin = Clientes()
contas = Conta()
menu = menu()
historico = Historico()

while True:
    admin.init()
    contas.init()
    while (menu.contin):
        historico.init()
        menu.principal()
    if menu.contin == False:
        break;

