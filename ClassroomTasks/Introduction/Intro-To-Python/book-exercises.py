import enum


section = input(
    "Escolha uma seção do livro para executar os exercícios (3-11): ")

print()

# Exercícios de String - 3.4
if (section == "3"):
    A = "Um elefante incomoda muita gente"
    print("Fatia correspondente à 'elefante incomoda': A[3:20]\n")

    string = input("Digite uma frase: ")
    print("Frase convertida: " + string.replace(" ", "").upper() + "\n")

# Exercícios de Números - 4.2
if (section == "4"):
    x = float(input("Digite um valor para X: "))
    y = float(input("Digite um valor para Y: "))

    if (abs(x) == abs(y)):
        print("Divisão por zero!\n")
    else:
        print("z = " + str((x ** 2 + y ** 2) / (x - y) ** 2) + "\n")

    salary = float(input("Digite o valor do salário: "))
    print("Novo salário: " + str(salary * 1.35))

# Exercícios de Listas - 5.5
if (section == "5"):
    L = [5, 7, 2, 9, 4, 1, 3]
    print("Tamanho da lista: " + str(len(L)))
    print("Maior valor da lista: " + str(max(L)))
    print("Menor Valor da lista: " + str(min(L)))
    print("Soma de todos os elementos da lista: " + str(sum(L)))
    L.sort()
    print("Lista em ordem crescente: ", L)
    L.reverse()
    print("Lista em ordem decrescente: ", L, "\n")

    print("Lista com múltiplos de 3 entre 1 e 50: " + str(list(range(3, 50, 3))))

# Exercícios de Dicionários - 7.2
if (section == "6" or section == "7"):
    dict = {
        "Salgado": 4.5,
        "Lanche": 6.5,
        "Suco": 3.0,
        "Refrigerante": 3.5,
        "Doce": 1.0
    }
    print("Dicionário criado: ", dict, "\n")

    grades = {
        "Verona": 9,
        "Cadu": 9.5,
        "Mace": 9.5,
        "Calors": 8.9,
        "Marcus": 8.5
    }
    print("Dicionário de notas: ", grades)
    print("Média das notas: ", sum(grades.values()) / len(grades.values()))

# Exercícios de Estrutura de decisão - 9.4
if (section == "8" or section == "9"):
    fstGrade = float(input("Digite a primeira nota do aluno: "))
    scndGrade = float(input("Digite a segunda nota do aluno: "))
    if ((fstGrade + scndGrade) / 2 >= 6):
        print("Aprovado!\n")
    else:
        print("Reprovado!\n")

    fstGrade = float(input("Digite a primeira nota do aluno: "))
    scndGrade = float(input("Digite a segunda nota do aluno: "))
    average = (fstGrade + scndGrade) / 2
    if (average > 6):
        print("Aprovado!")
    elif (average >= 4 and average <= 6):
        print("Exame!\n")
    else:
        print("Reprovado!")

# Exercícios de Estrutura de repetição - 10.3
if (section == "10"):
    S = 0
    for i in range(3, 334, 3):
        S += i
    print("S = " + str(S))

# Exercícios de Funções - 11.6
if (section == "11"):
    def drawLine(length):
        [print("_", end="") for _ in range(length)]
        print()
        print()

    def enumerateItems(list):
        [print("Item " + str(i) + ": " + str(list[i]))
         for i in range(len(list))]
        print()

    def mean(list):
        return (sum(list) / len(list))

    drawLine(10)
    enumerateItems(
        ["banana", 2.0, "IA", {"campo1": "Primeiro campo do dicionário"}])

    print("Média: ", mean([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
