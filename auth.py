from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required, logout_user, login_user
from .forms.form_login import LoginForm
from . import cursor, login_manager
from .models.usuario import Usuario

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm()
    usuario = form.usuario.data
    senha = form.senha.data
    sql = "SELECT * FROM usuario WHERE numFunc_us = (?) AND senha_us = (?);"
    cursor.execute(sql, [usuario, senha])
    res = cursor.fetchone()
    print(res)
    if res != None:
        usuario = Usuario()
        usuario.set_usuario(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])      
        login_user(usuario)
        return redirect(url_for('main.profile'))
    else:
        return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(id_usuario):
    print(id_usuario)
    if id_usuario is None:
        return redirect(url_for('auth.login'))
    else:
        sql = "SELECT * FROM usuario WHERE id_us = (?);"
        cursor.execute(sql, [id_usuario])
        res = cursor.fetchone()
        usuario = Usuario()
        usuario.set_usuario(res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7])
        return usuario
        