from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user
from models import get_db, Entrada, Comentario
from module002.forms import EntradaForm, ComentarioForm

module002 = Blueprint("module002", __name__, static_folder="static", template_folder="templates")

db = get_db()

@module002.route('/')
@login_required
def module002_index():
    if current_user.profile in ('admin', 'staff', 'student'):
        return render_template("module002_index.html", module='module002')
    else:
        #flash("Access Denied!")
        #return redirect(url_for('index'))
        abort(404,description="Page doesn't exist!")


@module002.route('/crear_entrada', methods=['GET','POST'])
@login_required
def module002_crear_entrada():
    form = EntradaForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            entrada = Entrada(titulo=form.titulo.data, cuerpo = form.cuerpo.data,user_id=current_user.id)
            db.session.add(entrada)
            try:
                db.session.commit()
                flash("Todo guay")
            except:
                db.session.rollback()
                flash("Error in database!")
        return redirect(url_for('module001.module001_index'))
    else:
        if current_user.profile in ('admin','staff','student'):
            return render_template("module002_crear_entrada.html",module="module002",form=form)
        else:
            flash("Access denied!")
            #abort(404,description="Access denied!")
            return redirect(url_for('index'))


@module002.route('/entradas')
@login_required
def module002_entradas():
    if current_user.profile in ('admin','staff','student'):
        entradas = Entrada.query.all()
        return render_template("module002_entradas.html",module="module002", rows=entradas)
    else:
        flash("Access denied!")
#        abort(404,description="Access denied!")
        return redirect(url_for('index'))


@module002.route('/entrada',methods=['GET','POST'])
@login_required
def module002_entrada():
    entrada = Entrada.query.filter_by(id=request.args.get('rowid')).first()
    if current_user.profile in ('admin','staff','student'):
        form = ComentarioForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                comentario = Comentario(cuerpo=form.cuerpo.data,user_id=current_user.id,entrada_id=entrada.id)
                db.session.add(comentario)
                try:
                    db.session.commit()
                    flash("Todo guay")
                except:
                    db.session.rollback()
                    flash("Error in database!")
                    return redirect(url_for('index'))
        comentarios = Comentario.query.filter_by(entrada_id = entrada.id)
        return render_template("module002_entrada.html",module="module002", entrada=entrada, comentarios=comentarios,form=form)
    else:
        flash("Access denied!")
#        abort(404,description="Access denied!")
        return redirect(url_for('index'))

@module002.route('/test')
def module002_test():
    return 'OK'