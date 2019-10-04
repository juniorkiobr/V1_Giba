# V1_Giba
Trabalho de para verificação de conteúdo na matéria de Lógica de Programação II


Segue-se alguns comandos do programa e suas respectivas funções:.

Clientes:.
  admin.init() - Inicializa a conexão com o banco de dados,
  admin.create() - Cria a tabela Clientes se não existir,
  admin.get_Dados() - Exibe os dados da tabela Clientes,
  admin.insert(nome, cpf, sexo) - Insere um novo cliente no banco de dados,
  admin.search(index) - Procura as informações de uma pessoa específica,
  admin.atualizarCliente(index) - Atualiza as informações de uma pessoa específica,
  admin.atualizarLista() - Atualiza a indexação da tabela Clientes,
  admin.remove(index) - Remove um cliente específico,
  admin.disconnect() - Encerra a conexão com o banco de dados,
  
Contas:.
  contas.init() - Inicializa a conexão com o banco de dados,
  contas.create() - Cria a tabela Contas se não existir,
  contas.adicionar(nrConta, cliente, HistoricoID) - Adiciona uma conta bancária,
  contas.extrato(index) - Exibe o extrato de uma conta bancária,
  contas.get_Dados() - Exibe as informações da tabela Contas,
  contas.deposita(index) - Deposita na respectiva conta bancária,
  contas.sacar(index) - Saca da respectiva conta bancária,
  contas.transferir(index, indexD) - Tranfere dinheiro de uma conta bancaria para outra,
  contas.remove(index) - Remove a conta bancária da tabela Contas,
  contas.atualizarLista(index) - Atualiza a indexação da tabela Clientes,
  contas.defLimite(index) - Define o limite de uma conta,
  contas.disconnect() - Encerra a conexão com o banco de dados,

Historico:.
  historico.init() - Inicializa a conexão com o banco de dados,
  historico.imprimir(index) - Imprime o histórico de transações da respectiva conta,
  historico.remove(index) - Remove uma única linha do histórico,
  historico.get_Dados() - Imprime a tabela Historico completa,
  historico.disconnect() - Encerra a conexão com o banco de dados,
