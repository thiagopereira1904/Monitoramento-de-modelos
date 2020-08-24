from wtforms import SelectField, StringField, DateField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from .. import cursor

def consultar_jornada():
    sql = "SELECT * FROM jornada;"
    cursor.execute(sql)
    resp = cursor.fetchall()
    opcoes = []
    for i in resp:
        opcoes.append(str(i[0]) + ' - ' + i[1])
    return opcoes

def consultar_responsavel():
    sql = 'SELECT * FROM usuario;'
    cursor.execute(sql)
    resp = cursor.fetchall()
    opcoes = []
    for i in resp:
        opcoes.append(i[1])
    return opcoes

def consultar_areaD():
    sql = 'SELECT * FROM area_demandante;'
    cursor.execute(sql)
    resp = cursor.fetchall()
    opcoes = []
    for i in resp:
        opcoes.append(str(i[0]) + ' - ' + i[1])
    return opcoes

def consultar_tipoM():
    sql = 'SELECT * FROM tipo_modelo;'
    cursor.execute(sql)
    resp = cursor.fetchall()
    opcoes = []
    for i in resp:
        opcoes.append(str(i[0]) + ' - ' + i[1])
    return opcoes


class CadastrarModelo(FlaskForm):
    nome_modelo = StringField('nome_modelo', validators=[DataRequired()])
    dataCad_modelo = DateField('dataCad_modelo', validators=[DataRequired()])
    diar_modelo = IntegerField('diar_modelo', validators=[DataRequired()])
    obs_modelo = StringField('obs_modelo')
    tipo_modelo = SelectField('tipo_modelo', choices=consultar_tipoM())
    area_demandante = SelectField('area_demandante', choices=consultar_areaD())
    jornada = SelectField('jornada', choices=consultar_jornada())
    responsavel = SelectField('responsavel', choices=consultar_responsavel())
    
    

