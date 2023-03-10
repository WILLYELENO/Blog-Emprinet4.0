from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from app.auth.decorators import admin_required
from app.auth.models import User
from app.models import Post
from . import admin_bp
from .forms import PostForm, UserAdminForm

@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    posts = Post.get_all()
    return render_template("admin/posts.html", posts=posts)


@admin_bp.route("/admin/post/", methods=['GET', 'POST'])
@login_required
@admin_required
def post_form():
    #   Crea un nuevo post   #
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()
        return redirect(url_for('admin.index'))
    return render_template("admin/post_form.html", form=form)

@admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_post_form(post_id):
    #   Actualiza un post existente   
    post = Post.get_by_id(post_id)
    if post is None:
        abort(404)
    # Crea un formulario inicializando los campos con los valores del post.
    form = PostForm(obj=post)
    if form.validate_on_submit():
        # Actualiza los campos del post existente
        post.title = form.title.data
        post.content = form.content.data
        post.save()
        return redirect(url_for('admin.index'))
    return render_template("admin/post_form.html", form=form, post=post)

@admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_post(post_id):
    post = Post.get_by_id(post_id)
    if post is None:
        abort(404)
    post.delete()
    return redirect(url_for('admin.index'))

