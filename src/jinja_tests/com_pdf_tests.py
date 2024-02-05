import logging
from jinja2 import Environment, FileSystemLoader
from pdfkit import from_string


def criar_pdf():
    """Função que popula um template através dos pacotes jinja2 e pdfkit."""

    env = Environment(loader=FileSystemLoader("src/jinja_tests/templates"))

    template_variaveis = {
        'nome': 'Joao Otavio',
        'processo': 'ddkcc 8855/2025'
    }

    template_output = env.get_template("test.html").render(template_variaveis)

    return from_string(
        template_output, False, css=["src/jinja_tests/styles/template.css"]
    )


def salvar_pdf(conteudo_pdf) -> None:
    """Função que salva o pdf na pasta out através de um parâmetro que pode 
    ser criado através da função criar_pdf()."""

    try:
        with open("src/jinja_tests/out/resultado.pdf", 'wb+') as pdf:
            pdf.write(conteudo_pdf)
    except Exception as error:  # pylint: disable=W0718:broad-exception-caught
        logging.error("Falha ao salvar o arquivo. Erro: %s", error)


def main():
    """Inicia a execução do processo de criação do pdf"""
    conteudo_pdf = criar_pdf()
    salvar_pdf(conteudo_pdf=conteudo_pdf)
    print("Arquivo salvo com sucesso!")


if __name__ == '__main__':
    main()
