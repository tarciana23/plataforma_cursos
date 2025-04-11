import time
import requests
from requests.exceptions import RequestException

curso_url = "http://localhost:8001/cursos" 
aluno_url = "http://localhost:8002/alunos" 
professor_url = "http://localhost:8003/professores"  


def consumir_cursos(categoria=None):
    try:
        if categoria:
            response = requests.get(curso_url, params={"categoria": categoria})  
        else:
            response = requests.get(curso_url)  
        
        print(f"Status code de cursos: {response.status_code}")
        
        if response.status_code == 200:
            cursos = response.json()
            if cursos:
                return cursos  
            else:
                print("Não foram encontrados cursos.")
                return None
        else:
            print(f"Erro ao acessar o microsserviço de cursos: {response.status_code}")
            print("Resposta:", response.text) 
            return None
    except RequestException as e:
        print(f"Erro ao acessar o microsserviço de cursos: {e}")
        return None

def consumir_alunos():
    try:
        response = requests.get(aluno_url)  
        print(f"Status code de alunos: {response.status_code}")
        if response.status_code == 200:
            return response.json()  
        else:
            print(f"Erro ao acessar o microsserviço de alunos: {response.status_code}")
            print("Resposta:", response.text)  
            return None
    except RequestException as e:
        print(f"Erro ao acessar o microsserviço de alunos: {e}")
        return None
    

def consumir_professores():
    try:
        response = requests.get(professor_url)
        print(f"Status code de professores: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erro ao acessar o microsserviço de professores: {response.status_code}")
            print("Resposta:", response.text)
            return None
    except RequestException as e:
        print(f"Erro ao acessar o microsserviço de professores: {e}")
        return None



def consumir_servicos():
    while True:
        print("\nConsumindo microsserviços...\n")

        cursos = consumir_cursos()
        if cursos:
            print("Cursos encontrados:", cursos)
        else:
            print("Não foi possível obter cursos no momento. Tentando novamente...")

        alunos = consumir_alunos()
        if alunos:
            print("Alunos cadastrados:", alunos)
        else:
            print("Não foi possível obter alunos no momento. Tentando novamente...")

        professores = consumir_professores()
        if professores:
            print("Professores cadastrados:", professores)
        else:
            print("Não foi possível obter professores no momento. Tentando novamente...")

        print("\nAguardando próximo ciclo...\n")
        time.sleep(5)

if __name__ == "__main__":
    consumir_servicos()