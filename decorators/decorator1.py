@app.route('/about')
def about():
    return render_template('about.html')