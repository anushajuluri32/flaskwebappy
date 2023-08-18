from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Cab
from . import db
import json
from datetime import datetime


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    '''
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 
        cab=request.form.get('cab')
        expirydate=request.form.get('expirydate')
        owner1 = request.form.get('owner')
        apartmentno1 = request.form.get('apartmentno')
        relativeof1 = request.form.get('relativeof')
        if cab==None and len(note)>=1:
            new_note = Note(data=note,owner=owner1,apartmentno=apartmentno1,user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Vehicle Number added!', category='success') 
        else:
            expirydate=expirydate.replace('T',':')
            expirydate = datetime.strptime(expirydate,'%Y-%m-%d:%H:%M')
            new_cab = Cab(data=cab,expdate=expirydate,relativeof=relativeof1, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_cab) #adding the note to the database 
            db.session.commit()
            flash('Vehicle Number added!', category='success')'''
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
@views.route('/delete-cab', methods=['POST'])
def delete_cab():  
    cab = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    cabId = cab['cabId']
    cab = Cab.query.get(cabId)
    if cab:
        if cab.user_id == current_user.id:
            db.session.delete(cab)
            db.session.commit()

    return jsonify({})

@views.route('/addnote', methods=['GET', 'POST'])
@login_required
def addnote():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 
        #cab=request.form.get('cab')
        #expirydate=request.form.get('expirydate')
        owner1 = request.form.get('owner')
        apartmentno1 = request.form.get('apartmentno')
        #relativeof1 = request.form.get('relativeof')
        if len(note)>=1:
            new_note = Note(data=note,owner=owner1,apartmentno=apartmentno1,user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Vehicle Number added!', category='success') 
    return render_template("addnote.html", user=current_user)

@views.route('/addcab', methods=['GET', 'POST'])
@login_required
def addcab():
    if request.method == 'POST': 
        #note = request.form.get('note')#Gets the note from the HTML 
        cab=request.form.get('cab')
        expirydate=request.form.get('expirydate')
        #owner1 = request.form.get('owner')
        #apartmentno1 = request.form.get('apartmentno')
        relativeof1 = request.form.get('relativeof')
        expirydate=expirydate.replace('T',':')
        expirydate = datetime.strptime(expirydate,'%Y-%m-%d:%H:%M')
        new_cab = Cab(data=cab,expdate=expirydate,relativeof=relativeof1, user_id=current_user.id)  #providing the schema for the note 
        db.session.add(new_cab) #adding the note to the database 
        db.session.commit()
        flash('Vehicle Number added!', category='success')
    return render_template("addcab.html", user=current_user)