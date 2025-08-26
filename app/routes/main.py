from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models import Cafe

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cafes = Cafe.query.all()
    return render_template('index.html', cafes=cafes)

@main.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        has_wifi = True if request.form.get('wifi') == 'on' else False
        has_coffee = True if request.form.get('coffee') == 'on' else False

        new_cafe = Cafe(name=name, location=location, has_wifi=has_wifi, has_coffee=has_coffee)
        db.session.add(new_cafe)
        db.session.commit()
        flash(f"Cafe '{name}' added successfully!", 'success')
        return redirect(url_for('main.index'))

    return render_template('add_cafe.html')

@main.route('/delete/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe = Cafe.query.get_or_404(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    flash(f"Cafe '{cafe.name}' deleted!", 'danger')
    return redirect(url_for('main.index'))

