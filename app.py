from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetAddForm, PetEditForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "lostsnlotsofpets!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Render and process form to add pet to database"""
    form = PetAddForm()
    if form.validate_on_submit():
        pet = Pet()
        form.populate_obj(pet)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {form.species.data} named {form.name.data}")
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/<int:id>', methods=['GET','POST'])
def view_edit_pet(id):
    """Show and process pet detail and edit form."""
    pet = Pet.query.get_or_404(id)
    form = PetEditForm(obj=pet)
    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()

        flash(f"Updated {pet.species} named {pet.name}")
        return redirect(f'/{id}')
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)
    