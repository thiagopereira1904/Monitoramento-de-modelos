from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from .forms.form_usuario import CadastrarUsuario
from .forms.form_modelo import CadastrarModelo
from . import cursor

main = Blueprint('main', __name__)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.NumFunc_us)

@main.route('/registrar_usuario')
@login_required
def registrar_usuario():
    register = CadastrarUsuario()
    return render_template('registrar_usuario.html', register=register, name=current_user.NumFunc_us)

@main.route('/registrar_usuario', methods=['POST'])
@login_required
def registrar_usuario_post():
    register = CadastrarUsuario()
    numFun = register.numeroFunc_usuario.data.upper()
    email =  register.email_usuario.data.upper()
    nome = register.nome_usuario.data.upper()
    jornada = int(register.id_jornada.data[0])
    tipo_usuario = int(register.tipo_usuario.data[0])
    funcao = int(register.funcao_usuario.data[0])
    sql = "SELECT * FROM usuario WHERE numFunc_us = (?);"
    cursor.execute(sql, [numFun])
    registros = cursor.fetchall()
    if len(registros) > 1:
        flash("USUÁRIO EXISTENTE!", "warning")
        return redirect(url_for('main.registrar_usuario'))
    else:
        sql = "INSERT INTO usuario (numFunc_us, email_us, nome_us, id_jd, id_tu, id_fu) VALUES (?, ?, ?, ?, ?, ?);"
        cursor.execute(sql, [numFun, email, nome, jornada, tipo_usuario, funcao])
        cursor.commit()
        flash("USUÁRIO CADASTRADO COM SUCESSO!", "success")
        return redirect(url_for('main.profile'))


@main.route('/usuarios')
@login_required
def usuarios():
    sql = "SELECT usuario.id_us, usuario.numFunc_us AS N_FUNC, usuario.email_us AS EMAIL, usuario.nome_us AS NOME, jornada.nome_jd as JORNADA FROM usuario INNER JOIN jornada ON usuario.id_jd = jornada.id_jd;"
    cursor.execute(sql)
    lista_usuarios = cursor.fetchall()
    return render_template('listar_usuarios.html', name=current_user.NumFunc_us, lista_usuarios=lista_usuarios)

@main.route('/excluir_usuario/<funcional>', methods=["GET"])
@login_required
def excluir_usuario(funcional):
    sql = "DELETE FROM usuario WHERE numFunc_us = (?);"
    cursor.execute(sql, [funcional])
    cursor.commit()
    return redirect(url_for('main.usuarios'))


@main.route('/registrar_modelo')
@login_required
def registrar_modelo():
    form = CadastrarModelo()
    return render_template('registrar_modelo.html', form=form, name=current_user.NumFunc_us)

    