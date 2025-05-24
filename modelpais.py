import requests
from tabelaPaises import inserirpais, listarpaises, zerartabela
from database import dbpais, paises

with paises.app_context():
    dbpais.create_all()


def gerenciarpaises():
    countries = {}
    contador = 0
    while contador < 3:  # enquanto não tiver digitado 3 países
        country = input("Digite o nome de um país: ")
        response = requests.get(f"https://restcountries.com/v3.1/name/{country}")

        if response.status_code == 200:
            contador += 1
        else:

            print(f"Erro: País '{country}' não encontrado na API.")
            continue

        datas = response.json()

        for data in datas:
            try:
                chave = data.get("name", {}).get("common", country.capitalize())
                moeda_key = next(iter(data.get("currencies", {})), None)
                idioma_key = next(iter(data.get("languages", {})), None)

                countries[chave] = {
                    "Nome_Comum": data.get("name", {}).get("common", 'ausente'),
                    "Nome_Oficial": data.get("name", {}).get("official", 'ausente'),
                    "Capital": data.get("capital", ['ausente'])[0] if data.get("capital") else 'ausente',
                    "Regiao": data.get("region", 'ausente'),
                    "Sub_regiao": data.get("subregion", 'ausente'),
                    "Populacao": data.get("population", 0),
                    "Moeda": {
                        "Simbolo": data.get("currencies", {}).get(moeda_key, {}).get("symbol",
                                                                                     'ausente') if moeda_key else 'ausente',
                        "Nome": data.get("currencies", {}).get(moeda_key, {}).get("name",
                                                                                  'ausente') if moeda_key else 'ausente'
                    },
                    "Idioma_Principal": data.get("languages", {}).get(idioma_key,
                                                                      'ausente') if idioma_key else 'ausente',
                    "Fuso_Horarios": ", ".join(data.get("timezones", [])) or 'ausente',
                    "Bandeira": data.get("flags", {}).get("png", 'ausente')
                }

                verificacao = inserirpais(countries[chave])
                if verificacao:
                    print(f"Deu tudo certo! País {chave} adicionado ao banco de dados!")

                else:
                    print(f"Algo deu errado... País {chave} não foi adicionado...")

            except AttributeError:
                print(f"O nome '{country}' pode estar errado ou não está de acordo com a API.")
                print("Tente novamente.")


if __name__ == "__main__":
    print("""
***ALERTA***
Este menu é para os desenvolvedores da aplicação.
Para fazer a tarefa da AP2, utilize o arquivo app.py""")
    while True:
        opcao = int(input("""
    MENU DE OPÇÕES: 
    [ 1 ] Listar Paises.
    [ 2 ] Zerar Tabela.
    [ 3 ] Testar insercao
    [ 4 ] Encerrar
    → """))
        if opcao == 1:
            listarpaises()

        elif opcao == 2:
            zerartabela()

        elif opcao == 3:
            gerenciarpaises()

        elif opcao == 4:
            break

        else:
            print("opcao invalida")
