from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, current_user
from .forms.form_usuario import CadastrarUsuario

main = Blueprint('main', __name__)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.NumFunc_us)

@main.route('/registrar_usuario')
@login_required
def registrar_usuario():
    register = CadastrarUsuario()
    return render_template('registrar_usuario.html', register=register)

@main.route('/registrar_usuario', methods=['POST'])
@login_required
def registrar_usuario_post():
    register = CadastrarUsuario()
    numFun = register.numeroFunc_usuario.data
    email =  register.email_usuario.data
    nome = register.nome_usuario.data
    funcao = int(register.funcao_usuario.data[0])
    jornada = int(register.id_jornada.data[0])
    tipo_usuario = int(register.tipo_usuario.data[0])
    print(numFun, email, nome, funcao, jornada, tipo_usuario)
    return redirect(url_for('main.profile'))

@main.route('/registrar_modelo')
@login_required
def registrar_modelo():
    return render_template('registrar_modelo.html')
    