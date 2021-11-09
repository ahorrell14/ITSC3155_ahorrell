
@app.route('/notes')
def get_notes():

	a_user = db.session.query(User).filter_by(email='ahorrell@uncc.edu').one()

	my_notes = db.session.query(Note).all()

	return render_template('notes.html', notes=my_notes, user=a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):

	a_user = db.session.query(User).filter_by(email='ahorrell@uncc.edu').one()

	my_note = db.session.query(Note).filter_by(id=note_id).one()

	return render_template('note.html', note=my_note, user=a_user)

@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():

	if request.method == 'POST':
		title = request.form['title']
		text = request.form['noteText']
		from datetime import date
		today = date.today()
		today = today.strftime("%m-%d-%Y")
		new_record = Note(title, text, today)
		db.session.add(new_record)
		db.session.commit()

		return redirect(url_for('get_notes'))
	else:
		a_user = db.session.query(User).filter_by(email='ahorrell@uncc.edu').one()
		return render_template('new.html', user = a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
