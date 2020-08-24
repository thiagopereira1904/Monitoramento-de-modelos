from wtforms import StringField, IntegerField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from .. import cursor



def consultar_jornada():
    sql = "SELECT * FROM jornada;"
    cursor.execute(sql)
    resp = cursor.fetchall()
    opcoes = []
    for i in resp:
        opcoes.append(str(i[0]) + ' - ' + i[1])
    return opcoes

def consultar_funcao():
    sql = "SELECT * FROM funcao_usuario;"
    cursor.execute(sql)
    resp1 = cursor.fetchall()
    opcoes_funcao = []
    for f in resp1:
        opcoes_funcao.append(str(f[0]) + ' - ' + f[1])
    return opcoes_funcao

def consultar_tu():
    sql = "SELECT * FROM tipo_usuario;"
    cursor.execute(sql)
    resp1 = cursor.fetchall()
    opcoes_tu = []
    for g in resp1:
        opcoes_tu.append(str(g[0]) + ' - ' + g[1])
    return opcoes_tu

class CadastrarUsuario(FlaskForm):
    nome_usuario = StringField('nome_usuario', validators=[DataRequired()])
    senha_usuario = StringField('senha_usuario', validators=[DataRequired()])
    numeroFunc_usuario = StringField('senha_usuario', validators=[DataRequired(), Length(min=7, max=7)])
    email_usuario = StringField('email_usuario', validators=[DataRequired()])
    funcao_usuario = SelectField('funcao_usuario', validators=[DataRequired()], choices=consultar_funcao())
    sessao_usuario = IntegerField('sessao_usuario', validators=[DataRequired()])
    tipo_usuario = SelectField('tipo_usuario', validators=[DataRequired()], choices=consultar_tu())
    id_jornada = SelectField('id_jornada', validators=[DataRequired()], choices=consultar_jornada(), default="Selecione:")