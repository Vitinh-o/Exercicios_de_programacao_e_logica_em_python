from pprint import pprint
import os 

list_tasks = []
deleted_tasks = []

def insert_task(task):

    list_tasks.append(task)

def delete_task():

    if not list_tasks:
        print("Nenhum item para deletar")

    else:    
        task = list_tasks.pop()

        deleted_tasks.append(task)

def undo_task():

    if not deleted_tasks:
        print("Nenhuma ação para desfazer")

    else:

        task = deleted_tasks.pop()

        list_tasks.append(task)


def save_list_file():
    
    os.system("cls")

    if not list_tasks:
        print("Nenhum item para salvar")
        return None

    with open("lista.txt", "w+") as file:
        
        for tasks in list_tasks:
        
            file.write(f"{tasks} \n")  


def load_list_file():

    try:

        with open("lista.txt", "r", encoding="utf-8") as file:
    
            for line in file:
                task = line.strip()
                list_tasks.append(task)

    
    except FileNotFoundError:
        
        if not list_tasks:
            
            return None




def list_print():
        
    for tasks in list_tasks:
        pprint(tasks)


load_list_file()

while True:

    print("Bem-vindo ao criador de tarefas")
    print("Digite uma das opções: abaixo.")
    option = input("inserir, apagar, desfazer, salvar ou finalizar: ").lower()

    if option == "inserir":

        os.system("cls")
        digited_task = input("Digite a tarefa: ")

        insert_task(digited_task) 


        list_print()

    elif  option == "apagar":


        os.system("cls")
        delete_task()

        list_print()

    elif option == "desfazer":

        os.system("cls")
        undo_task()

        list_print()
 

    elif option == "salvar":

        save_list_file()


    elif option == "finalizar":

        print("Encerrado o programa")
        break

    else:

        os.system("cls")
        print("Você não digitou uma opção válida")
