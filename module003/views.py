from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user

from models import get_db, User, Tarea

from module003.forms import *

module003 = Blueprint("module003", __name__,static_folder="static",template_folder="templates")

@module003.route('/')
def module003_index():
    return render_template("module003_index.html",module='module003')

@module003.route('/crear_tarea', methods=['GET','POST'])
@login_required
def module003_crear_tarea():
    form = TareaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            tarea = Tarea(titulo=form.titulo.data, contenido = form.contenido.data)
            db.session.add(tarea)
            try:
                db.session.commit()
                flash("Todo guay")
            except:
                db.session.rollback()
                flash("Error in database!")
        return redirect(url_for('module003.module003_index'))
        pass
    else:
        if current_user.profile in ('admin','staff'):
            return render_template("module003_crear_tarea.html",module="module003", form=form)
        else:
            flash("Access denied!")
    #        abort(404,description="Access denied!")
            return redirect(url_for('index'))

@module003.route('/test')
def module003_test():
    return 'OK'