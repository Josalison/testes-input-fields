import httpx
import json

url_usuario = ('https://jsonplaceholder.typicode.com/posts/1')
response = httpx.request('get', url_usuario)

dados = response.json()

print(json.dumps(dados, indent=4))

assert response.status_code==200, "Erro o status não foi 200!!! "
assert dados["id"]==1, "Erro: o id retornado não e numero 1"

print("✅ Teste com sucesso: O usuário existe e é o ID 1!")