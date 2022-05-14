from psycopg2 import connect
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


def init_app(app):
  db = psycopg2.connect("dbname='mkData3.0' user='' host='' password=''")

  try:
    cur = db.cursor()
    cur.execute("""SELECT os.codos, df.descricao_defeito, tp.descricao, os.data_abertura, cl.nome_razaosocial, cd.cidade, ba.bairro
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
      JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
      WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")
    db = cur.fetchall()
    return db
  except:
    return "Impossible to connect to the database, check your code."