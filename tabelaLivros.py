from database import dblivro as db
from database import livros as app


class Livros(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    preco = db.Column(db.String(200), nullable=False)
    avaliacao = db.Column(db.String(200), nullable=False)
    disponibilidade = db.Column(db.String(200), nullable=False)


def inserirlivro(title, price, aval, disp):
    with app.app_context():
        try:
            novo_livro = Livros(
                titulo=title,
                preco=price,
                avaliacao=aval,
                disponibilidade=disp
            )

            db.session.add(novo_livro)
            db.session.commit()
            print(f"Livro {title} adicionado com sucesso!")
            return True

        except:
            print(f"Algo deu errado e o livro {title} não foi adicionado...")
            return False


def listarlivros():
    with app.app_context():
        livros = Livros.query.all()
        for livro in livros:
            print(f"[{livro.id}] - {livro.titulo} | {livro.preco} | {livro.disponibilidade} | {livro.avaliacao} | ")


def zerartabela():
    with app.app_context():
        livros = Livros.query.all()
        for livro in livros:
            db.session.delete(livro)
            db.session.commit()


if __name__ == '__main__':
    pass
