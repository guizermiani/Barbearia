from functools import wraps
from flask import Flask, redirect, session, url_for

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'usuario_logado' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def login_required_cliente(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'cliente_logado' not in session:
            return redirect(url_for('login_cliente'))
        return f(*args, **kwargs)
    return decorated