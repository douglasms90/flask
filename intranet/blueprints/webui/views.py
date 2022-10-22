from flask import abort, render_template

from intranet.ext.database import dbConn
from intranet.ext.forms import commForms


def index():
  form = commForms()
  conn = dbConn()
  if form.comm.data == 'os':
    rows = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, to_char(os.data_abertura, 'dd/mm/yyyy'), cl.nome_razaosocial, cd.cidade, ba.bairro
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      JOIN mk_cidades cd ON os.cd_cidade = cd.codcidade
      JOIN mk_bairros ba ON os.cd_bairro = ba.codbairro
      WHERE status='1' AND tipo_os in ('4','15','18') AND fechamento_tecnico='N' ORDER BY cd.cidade asc""")
    title = ('ID', 'DEFEITO', 'TIPO', 'GERADA', 'CLIENTE', 'CIDADE', 'BAIRRO') 
    return render_template("index.html", form=form, rows = rows, ts = title)
  if form.comm.data == 're':
    rows = conn.consult("""SELECT os.codos, df.descricao_defeito, tp.descricao, to_char(os.data_fechamento, 'dd/mm/yyyy'), cl.nome_razaosocial, os.operador_fech_tecnico, os.servico_prestado
      FROM mk_os os
      FULL OUTER JOIN mk_os_tipo tp ON os.tipo_os = tp.codostipo
      JOIN mk_pessoas cl ON os.cliente = cl.codpessoa
      JOIN mk_os_defeitos df ON os.defeito_associado = df.coddefeito
      WHERE  tipo_os in ('4','15','18') AND data_fechamento = CURRENT_DATE AND servico_prestado LIKE '%ugl%' ORDER BY os.data_fechamento desc""")
    title = ('ID', 'DEFEITO', 'DESCRIÇÃO', 'FECHAMENTO', 'CLIENTE', 'OPERADOR', 'DESCRIÇÃO')
    return render_template("index.html", form=form, rows = rows, ts = title)
  return render_template("index.html", form=form)
