from db.database import Database
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("src/jinja_tests/templates"))
template = env.get_template(name="processo.html.jinja")

SQL = "select * from production.brands"
instance = Database()
conn = instance.connect()
cursor = conn.cursor()
cursor.execute(SQL)

templ_vars = dict(brand=cursor.fetchall())
SQL = "SELECT * FROM production.products WHERE product_id = 1"
cursor.execute(SQL)
dados = cursor.fetchone()
 
templ_vars.update(produto=dados)

print(template.render(templ_vars))

instance.fechar_conexao(cursor=cursor, conexao=conn)
