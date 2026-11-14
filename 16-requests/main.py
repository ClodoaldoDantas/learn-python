import requests


def get_user():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        user = response.json()
        print("Nome do usuário:", user.get('name'))
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro de conexão: {e}")

get_user()
