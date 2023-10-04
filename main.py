#Programa sistema de gestão para controle de horários de aula - Cláudio Pereira
# BSI - Algoritmos e Lógica de Programação
import pickle
import os

def salvar(): # função para poder salvar por cima do arquivo anterior
  with open("database.dat","wb") as arquivo:
    pickle.dump(turmas, arquivo)

def hora_disponivel():
  horarios = {"2M12" : "7:00 - 8:40",
              "2M34" : "8:55 - 10:35",
              "2M56" : "10:50 - 12:30",
              "2T12" : "13:00 - 14:40",
              "2T34" : "14:55 - 16:35",
              "2T56" : "16:50 - 18:30",
              "2N12" : "18:45 - 20:25",
              "2N34" : "20:35 - 22:15",
              "3M12" : "7:00 - 8:40",
              "3M34" : "8:55 - 10:35",
              "3M56" : "10:50 - 12:30",
              "3T12" : "13:00 - 14:40",
              "3T34" : "14:55 - 16:35",
              "3T56" : "16:50 - 18:30",
              "3N12" : "18:45 - 20:25",
              "3N34" : "20:35 - 22:15",
              "4M12" : "7:00 - 8:40",
              "4M34" : "8:55 - 10:35",
              "4M56" : "10:50 - 12:30",
              "4T12" : "13:00 - 14:40",
              "4T34" : "14:55 - 16:35",
              "4T56" : "16:50 - 18:30",
              "4N12" : "18:45 - 20:25",
              "4N34" : "20:35 - 22:15",
              "5M12" : "7:00 - 8:40",
              "5M34" : "8:55 - 10:35",
              "5M56" : "10:50 - 12:30",
              "5T12" : "13:00 - 14:40",
              "5T34" : "14:55 - 16:35",
              "5T56" : "16:50 - 18:30",
              "5N12" : "18:45 - 20:25",
              "5N34" : "20:35 - 22:15",
              "6M12" : "7:00 - 8:40",
              "6M34" : "8:55 - 10:35",
              "6M56" : "10:50 - 12:30",
              "6T12" : "13:00 - 14:40",
              "6T34" : "14:55 - 16:35",
              "6T56" : "16:50 - 18:30",
              "6N12" : "18:45 - 20:25",
              "6N34" : "20:35 - 22:15",
           }
  return horarios

#Tenta dar load nos dados salvos, mas caso não exista e para não dar crash no programa, ele cria uma lista vazia nova para não dar conflito.
try:
  with open("database.dat", "rb") as arquivo:
    turmas_salvas = pickle.load(arquivo)
except:
     turmas_salvas = {} # Tive Ajuda do chat GPT para tentar criar lista vazia no lugar para não dar erro

turmas = dict(turmas_salvas) # dict() cria dicionário da variável


def interface():
  os.system('clear') # Apaga os comandos ateriores para ficar mais "limpo"
  print("\t========================================")
  print("\t============ Menu Principal ============")
  print("\t========================================")
  print()
  print("\t# Digite o Menu que deseja: ")
  print("\t# 1 - Menu Professor")
  print("\t# 2 - Menu Aluno")
  print("\t# 3 - Informações do Programa")
  print("\t# 0 - Sair do Programa")
  print()
  sis = int(input("\tDigite sua opção: "))
  print()
  return sis

def menu_aluno():
  os.system('clear')
  print("\t========================================")
  print("\t============== Menu Aluno ==============")
  print("\t========================================")
  print()
  print("\t# Digite a função que deseja")
  print("\t# 1 - Procurar Turma")
  print("\t# 2 - Listar Todas as Turmas")
  print("\t# 0 - Sair da Aba")
  print()
  sis = int(input("\tDigite sua opção: "))
  print()
  return sis

def menu_professor():
  os.system('clear')
  print("\t========================================")
  print("\t============ Menu Professor ============")
  print("\t========================================")
  print()
  print("\t# Digite a função que deseja")
  print("\t# 1 - Cadastrar Turma")
  print("\t# 2 - Procurar Turma")
  print("\t# 3 - Listar Todas as Turmas")
  print("\t# 4 - Excluir Turma")
  print("\t# 5 - Atualizar Turma")
  print("\t# 0 - Sair da Aba")
  print()
  sis = int(input("\tDigite sua opção: "))
  print()
  return sis

def creditos():
  os.system("clear")
  print("\t=========================================")
  print("\t======== Informações do Programa ========")
  print("\t=========================================")
  print()
  print("\tProjeto sobre Gestão de Controle de Aulas")
  print("\tpatrocinado pelo docente Flávius Gorgonio")
  print("\tprofessor do curso de Algoritmos e Lógica")
  print("\tde Programação, tendo como função um meio")
  print("\tde organizar e ter o controle de horários")
  print("\tde aulas de uma maneira simples por meio ")
  print("\tdo programa apresentado.")
  print()
  print("\t=========================================")
  print("\t# Desenvolvido por Cláudio Pereira Teixeira de Araújo")
  print("\t# Bacharelado de Sistemas de Informação - UFRN CERES")
  print()
  input("(Pressione Enter para sair.)")

def validacao_turma(tur): # Verifica se Já existe alguma turma cadastrada com o mesmo nome
  i = True
  while i == True:
    if tur in turmas:
      tur = input("Digite um nome de turma que ainda não existe: ")
    else:
      i = False

def validacao_materia(tur,mate):
  i = True
  while i == True:
    if mate in turmas[tur]:
      mate = input("Digite um nome de uma Matéria que ainda não esteja cadastrada: ")
    else:
      return mate

def cadastro_turma():
  horarios = hora_disponivel() # Cria um novo Dicionário de horários para cada turma diferente
  k = True
  while k == True:
    print()
    print("# Turmas Existentes: ")
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    tur = input("Escreva o Período/Nome da turma: \nExemplo: DCT1011\n- ")
    validacao_turma(tur)
    materias = {}
    print()
    mate = True
    while mate == True:
      mate = input("\tInsira o nome da matéria: ")
      print()
      verify = input("\tDeseja ver os horários disponíveis?(S/N) ") #Chave para entrar em ciclo para ver disponibilidade dos dias
      verify = verify.upper()
      print()
      while verify == "S":
        disp = input("\tQual dia deseja verificar?\n(segunda, terça, quarta, quinta, sexta)\n- ")
        print() # Usa o dicionário Horários para checar a disponibilidade dos horários que vão estar disponíveis 
        if disp.lower() == "segunda":
          for sigla in horarios:
            if sigla.startswith("2"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "terça":
          for sigla in horarios:
            if sigla.startswith("3"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "quarta":
          for sigla in horarios:
            if sigla.startswith("4"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "quinta":
          for sigla in horarios:
            if sigla.startswith("5"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "sexta":
          for sigla in horarios:
            if sigla.startswith("6"):
              print(sigla,":",horarios[sigla])
              print()
        else:
          print("***INFORME ITEM VÁLIDO***\n")
          print()
        verify = input("\tDeseja ver de novo os horários disponíveis?(S/N) ")
        verify = verify.upper()
        print()
      
      h = True
      while h == True:
        escolha = input("Digite uma das siglas disponíveis para cadastrar na matéria: ")
        escolha = escolha.upper()
        print()
        if escolha in horarios:
          del horarios[escolha] # Deleta horário no dicionário de Horários para não poder adicionar 2 horários iguais a mesma matéria e não dar conflito.
          materias[mate] = [] # Cria uma lista para a matéria escolhida e poder adicionar os horários dentro
          materias[mate].append(escolha) # Adiciona o horário na lista criada
          turmas[tur] = materias # Adiciona o dicionário "materias" dentro do dicionário "turmas" na chave do nome da turma escolhida
          turmas[tur][mate].sort() # Organiza os horários em ordem crescente Ex(2, 3, 4, 5)
          print("\t##### Horário cadastrado! #####")
          h = False
        else:
          print("*** INSIRA ITEM VÁLIDO ***\nEx:2M12")
          
      
      print()
      horar = input("\tDeseja cadastrar mais dos horarios à mesma matéria?(S/N) ")
      horar = horar.upper()
      print()
      while horar == "S":
        print("Horários *NÃO* Disponíveis: ")
        for l in turmas[tur][mate]: # Mostra os horários na matéria que já existem na lista para consulta.
          print(l, end = ", ")
        print()
        print()
        escolha = input("Escolha um horário disponível para cadastrar na matéria: ")
        escolha = escolha.upper()
        if escolha in horarios:
          del horarios[escolha]
          materias[mate].append(escolha)
          turmas[tur] = materias
          turmas[tur][mate].sort() # Acontece mesma coisa doque antes, soque dessa vez não se cria outra lista vazia dentro da chave de matéria
          print("\t##### Horário cadastrado! #####")
        else:
          print("***INFORME ITEM VÁLIDO***")
        print()
        horar = input("\tDeseja cadastrar mais dos horarios à matéria?(S/N) ")
        horar = horar.upper()
        print()
      mate = input("\tDeseja cadastrar outra matéria na mesma turma?(S/N) ")
      mate = mate.upper() # Chave para sair ou não do laço
      print()
      if mate == "S":
        mate = True
      else:
        mate = False
    salvar()
    print("##### Turma Cadastrada! #####\n")
    k = False
  print()
  input("(Pressione Enter para sair.)")

def procurar_turma():
  i = True
  while i == True:
    print()
    print("# Turmas Disponíveis: ") # Mostra o nome das turmas para consulta
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    turm = input("\tDigite o nome exato da Turma que deseja buscar: ")
    print()
    if turm in turmas:
      print("="*40)
      print()
      print("Nome da Turma:", turm)
      for materia in turmas[turm]:
        print("Matéria:", materia)
        print("Horários: ")
        for listahoras in turmas[turm][materia]: # vai entrando nos laços para buscar os valores e dar print
          print("-",listahoras)
        print()
    else:
      print("\tTurma não existe/Digite o nome da mesma forma que cadastrou!")
    print()
    turm = input("\tDeseja procurar outra turma?(S/N) ")
    turm = turm.upper()
    if turm == "S":
      i = True
    elif turm != "S":
      i = False
      input("(Pressione Enter para sair.)")
  print()

def lista_tudo():
  for turm in turmas:
    print()
    print("="*40)
    print()
    print("Nome da Turma:", turm) # Faz o mesmo q a função de procurar turma, soque dessa vez não consulta o nome para buscar, apenas entra nos dicionários mostrando todos os valores e printando
    for materia in turmas[turm]:
      print("Matéria:", materia)
      print("Horários: ")
      for listahoras in turmas[turm][materia]:
        print("-",listahoras)
      print()
    print()
  input("(Pressione Enter para sair.)")

def exclui_turmas():
  x = True
  while x:
    print()
    print("# Turmas Disponíveis: ") # Mostra o nome das turmas para consulta
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    escolha = input("Digite exatamente o nome da turma que deseja apagar: ")
    print()
    if escolha in turmas:
      certe = input(f"Tem certeza que deseja apagar turma {escolha}?(S/N) ")
      print()
      certe = certe.upper()
      if certe == "S":
        del turmas[escolha]
        salvar()
        print("Turma Deletada!\n")
        x = False
      else:
        x = False
    else:
      print("Digite uma turma válida!!!")
  print()
  input("(Pressione Enter para sair.)")

def atualizacao_menu():
  os.system('clear')
  print("\t========================================")
  print("\t=         Menu de Atualização          =")
  print("\t========================================")
  print()
  print("\t# 1 - Atualizar nome de Turma")
  print("\t# 2 - Excluir Matéria")
  print("\t# 3 - Adicionar Matéria na Turma")
  print("\t# 4 - Remover Horário na Matéria")
  print("\t# 5 - Adicionar Horário na Matéria")
  print("\t# 0 - Sair da aba")
  print()
  escolha = int(input("\tDigite a opção que deseja: "))
  print()
  return escolha

def atualizacao_turma():
  print()
  escolha = 1
  while escolha != 0:
    escolha = atualizacao_menu()
    if escolha == 1:
      print("\t======== Atualizar nome de Turma =======")
      att_nome_turma()
    elif escolha == 2:
      print("\t============ Excluir Matéria ============")
      att_nome_materia()
    elif escolha == 3:
      print("\t====== Adicionar Matéria em Turma ======")
      add_materia_turma()
    elif escolha == 4:
      print("\t====== Remover Horário na Matéria ======")
      att_horario()
    elif escolha == 5:
      print("\t===== Adicionar Horário em Matéria =====")
      add_horario_materia()
    else:
      print("***INFORME ITEM VÁLIDO***\n")

def att_nome_turma():
  g = True
  while g == True:
    print()
    print("Turmas Disponíveis: ") # Mostra o nome das turmas para consulta
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    renome = input("\tQual turma deseja renomear? ")
    print()
    if renome in turmas:
      print(f"Qual novo nome deseja dar a turma {renome}?")
      novo_nome = input("- ")
      print()
      t_nova = turmas[renome] # Guarda os antigos valores em uma variável nova
      turmas[novo_nome] = t_nova # Depois coloca os valores antigos na chave que foi renomeada 
      #OBS: Tive auxilio do Chat GPT para aplicar isso da forma correta.
      del turmas[renome] # Deleto a chave de nome antigo.
      salvar()
      print("\t##### Nome Alterado! #####")
      print()
    else:
      print("\t*** INFORME TURMA EXISTENTE ***")
    laco = input("\tDeseja Atualizar outro nome de Turma?(S/N) ")
    laco = laco.upper()
    print()
    if laco != "S":
      g = False
  print()
  input("(Pressione Enter para sair.)")

def att_nome_materia():
  g = True
  while g == True:
    print()
    print("Turmas Disponíveis: ") # Mostra o nome das turmas para consulta
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    tur = input("Digite o nome da turma em que a matéria desejada está: ")
    print()
    if tur in turmas:
      print("Matérias Disponíveis: ")
      for i in turmas[tur]: # Mostra o nome das materias para consulta
        print(i, end=", ")
      print()
      print()
      mat_remove = input("Digite uma das Matérias acima para exlcuir: ")
      print()
      if mat_remove in turmas[tur]:
        del turmas[tur][mat_remove]
        salvar()
        print("##### Matéria Excluida! #####")
        print()
      else:
        print("*** Informe Matéria Existente! ***")
      print()
    else:
      print("*** DIGITE UMA TURMA EXISTENTE! ***")
      print()
    pergunta = input("Deseja Excluir mais matérias?(S/N) ")
    pergunta = pergunta.upper()
    if pergunta != "S":
      g = False
  print()
  print()
  input("(Pressione Enter para sair.)")

def add_materia_turma():
  x = True
  while x == True:
    print()
    print("Turmas Disponíveis: ") # Mostra o nome das turmas para consulta
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    horarios = hora_disponivel()
    tur = input("Digite a Turma em que deseja adicionar uma Matéria: ")
    if tur in turmas:
      materias = {}
      for i in turmas[tur]:
        for j in turmas[tur][i]:
          del horarios[j]         # Apaga os horarios que ja existem na turma ao todo para não ter repetição
      mate = input("\tInsira o nome da matéria: ")
      validacao_materia(tur,mate)
      print()
      verify = input("\tDeseja ver os horários disponíveis?(S/N) ")
      verify = verify.upper()
      print()
      while verify == "S":
        disp = input("\tQual dia deseja verificar?\n(segunda, terça, quarta, quinta, sexta)\n- ")
        print()
        if disp.lower() == "segunda":
          for sigla in horarios:
            if sigla.startswith("2"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "terça":
          for sigla in horarios:
            if sigla.startswith("3"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "quarta":
          for sigla in horarios:
            if sigla.startswith("4"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "quinta":
          for sigla in horarios:
            if sigla.startswith("5"):
              print(sigla,":",horarios[sigla])
              print()
        elif disp.lower() == "sexta":
          for sigla in horarios:
            if sigla.startswith("6"):
              print(sigla,":",horarios[sigla])
              print()
        else:
          print("***INFORME ITEM VÁLIDO***\n")
          print()
        verify = input("\tDeseja ver de novo os horários disponíveis?(S/N) ")
        verify = verify.upper()
        print()
        
      h = True
      while h == True:
        escolha = input("Digite uma das siglas disponíveis para cadastrar na matéria: ")
        escolha = escolha.upper()
        print()
        if escolha in horarios:
          del horarios[escolha]
          materias[mate] = []
          materias[mate].append(escolha)
          turmas[tur].update(materias)
          turmas[tur][mate].sort()
          print("\t##### Horário cadastrado! #####")
          h = False
        else:
          print("*** INSIRA ITEM VÁLIDO ***\nEx:2M12")
            
        
      print()
      horar = input("\tDeseja cadastrar mais dos horarios à mesma matéria?(S/N) ")
      horar = horar.upper()
      print()
      while horar == "S":
        print("Horários *NÃO* Disponíveis: ")
        for l in turmas[tur][mate]: # Mostra os horários na matéria que já existem na lista para consulta.
          print(l, end = ", ")
        print()
        print()
        escolha = input("Escolha o horário dos disponíveis para cadastrar na matéria: ")
        escolha = escolha.upper()
        if escolha in horarios:
          del horarios[escolha]
          materias[mate].append(escolha)
          turmas[tur].update(materias)
          turmas[tur][mate].sort()
          print("\t##### Horário cadastrado! #####")
        else:
          print("***INFORME ITEM VÁLIDO***")
        print()
        horar = input("\tDeseja cadastrar mais dos horarios à matéria?(S/N) ")
        horar = horar.upper()
        print() 
      salvar()
      print("##### Matéria Cadastrada! #####")
      print()
    else:
      print("*** Informe uma Turma existente!!! ***")
      print()
    pergunta = input("Deseja cadastrar mais matéria na turma existente?(S/N) ")
    pergunta = pergunta.upper()
    print()
    if pergunta != "S":
      x = False
  print()
  input("(Pressione Enter para sair.)")

def att_horario():
  x = True
  while x == True:
    print()
    print("# Turmas Disponíveis: ")
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    tur = input("\tDigite o nome da turma que deseja editar: ")
    print()
    if tur in turmas:
      print("# Matérias Disponíveis: ")
      for i in turmas[tur]:
        print(i, end=", ")
      print()
      print()
      mate = input("\tDigite o nome da Matéria em que o horário desejado está: ")
      if mate in turmas[tur]:
        print("# Horários Disponíveis:")
        for j in turmas[tur][mate]:
          print(j, end=", ")
        print()
        print()
        hora = input("\tEscolha um dos horários acima para deletar: ")
        hora = hora.upper()
        if hora in turmas[tur][mate]:
          turmas[tur][mate].remove(hora)
          turmas[tur][mate].sort()
          print()
          salvar()
          print("##### Horário Deletado! #####")
          print()
        else:
          print("*** Insira um Horário válido!!! ***")
          print()
      else:
        print("*** Insira Matéria válida!!! ***")
        print()
    else:
      print("*** Insira uma Turma válida!!! ***")
      print()
    pergunta = input("\tDeseja Remover mais horários?(S/N) ")
    pergunta = pergunta.upper()
    if pergunta != "S":
      x = False
  print()
  input("(Pressione Enter para sair.)")
    
  
def add_horario_materia():
  x = True
  while x == True:
    print()
    print("# Turmas Disponíveis: ")
    for i in turmas:
      print(i, end=", ")
    print()
    print()
    tur = input("\tDigite o nome da turma desejada: ")
    print()
    if tur in turmas:
      print("# Matérias Disponíveis: ") # Mostra o nome das matérias para consulta
      for i in turmas[tur]:
        print(i, end=", ")
      print()
      print()
      mate = input("\tDigite o nome da Matéria em que o horário desejado está: ")
      print()
      if mate in turmas[tur]:
        print("# Horários já existentes:") # Mostra o nome dos horários para consulta
        for j in turmas[tur][mate]:
          print(j, end=", ")
        print()
        print()
        hora = input("\tDigite um horário não existente para adicionar: ")
        hora = hora.upper()
        if hora not in turmas[tur][mate]:
          turmas[tur][mate].append(hora)
          turmas[tur][mate].sort()
          print()
          salvar()
          print("##### Horário Adicionado! #####")
          print()
        else:
          print("*** Insira um Horário válido!!! ***")
          print()
      else:
        print("*** Insira Matéria válida!!! ***")
        print()
    else:
      print("*** Insira uma Turma válida!!! ***")
      print()
    pergunta = input("Deseja Adicionar mais horários?(S/N) ")
    pergunta = pergunta.upper()
    if pergunta != "S":
      x = False
  print()
  input("(Pressione Enter para sair.)")

######################################### Programa Principal: ##########################################
print("\tControle de Horários de Aula")
sis = interface()
while sis != 0:
  if sis == 1:
    op_prof = menu_professor()
    while op_prof != 0:
      if op_prof == 1:
        print("\t"+"="*8,"Cadastramento de turma","="*8,"\n")
        cadastro_turma()
      elif op_prof == 2:
        print("\t"+"="*12,"Procurar Turma","="*12,"\n")
        procurar_turma()
      elif op_prof == 3:
        print("\t"+"="*7,"Lista de Todas as Turmas","="*7,"\n")
        lista_tudo()
      elif op_prof == 4:
        print("\t"+"="*12,"Excluir Turmas","="*12,"\n")
        exclui_turmas()
      elif op_prof == 5:
        print("\t"+"="*9,"Turma para Atualizar","="*9,"\n")
        atualizacao_turma()
      elif op_prof == 0:
        sis = 0
      else:
        print("***INFORME ITEM VÁLIDO***\n")
      op_prof = menu_professor()

  elif sis == 2:
    op_aluno = menu_aluno()
    while op_aluno != 0:
      if op_aluno == 1:
        print("\t"+"="*12,"Procurar Turma","="*12,"\n")
        procurar_turma()
      elif op_aluno == 2:
        print("\t"+"="*7,"Lista de Todas as Turmas","="*7,"\n")
        lista_tudo()
      elif op_aluno == 0:
        sis = 0
      else:
        print("***INFORME ITEM VÁLIDO***\n")
      op_aluno = menu_aluno()

  elif sis == 3:
    creditos()
      
  else:
    print("***INFORME ITEM VÁLIDO***\n")
  sis = interface()
print("Fim do programa!")