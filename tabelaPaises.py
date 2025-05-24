from database import dbpais as db
from database import paises as app


class Paises(db.Model):
    __tablename__ = 'paises'

    id = db.Column(db.Integer, primary_key=True)
    nome_comum = db.Column(db.String(200), nullable=False)
    nome_oficial = db.Column(db.String(200), nullable=False)
    capital = db.Column(db.String(200), nullable=False)
    regiao = db.Column(db.String(200), nullable=False)
    subregiao = db.Column(db.String(200), nullable=False)
    populacao = db.Column(db.Integer, nullable=False)
    moedaSimbolo = db.Column(db.String(200), nullable=False)
    moedaNome = db.Column(db.String(200), nullable=False)
    idioma = db.Column(db.String(200), nullable=False)
    fusoHorario = db.Column(db.String(200), nullable=False)
    bandeira = db.Column(db.String(200), nullable=False)


def inserirpais(json):
    with app.app_context():
        try:
            novo_pais = Paises(
                nome_comum=json["Nome_Comum"],
                nome_oficial=json["Nome_Oficial"],
                capital=json["Capital"],
                regiao=json["Regiao"],
                subregiao=json["Sub_regiao"],
                populacao=int(json["Populacao"]),
                moedaSimbolo=json["Moeda"]["Simbolo"],
                moedaNome=json["Moeda"]["Nome"],
                idioma=json["Idioma_Principal"],
                fusoHorario=json["Fuso_Horarios"],
                bandeira=json["Bandeira"]
            )
            db.session.add(novo_pais)
            db.session.commit()
            print("Pais Adicionado com Sucesso!")
            return True

        except KeyError as e:
            print(f"Erro: Está faltando: {e.args[0]} não encontrada!")
            return False

        except ValueError as e:
            print(f"Erro: Valor inválido - {e}")
            return False


def listarpaises():
    with app.app_context():
        paises = Paises.query.all()
        for pais in paises:
            print(f'[{pais.id}] - {pais.nome_comum} | {pais.nome_oficial} | {pais.regiao} | {pais.idioma} |')


def zerartabela():
    with app.app_context():
        paises = Paises.query.all()
        for pais in paises:
            db.session.delete(pais)
            db.session.commit()


if __name__ == '__main__':
    pass
