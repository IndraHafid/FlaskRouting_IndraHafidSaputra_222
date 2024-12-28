from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    if request.method == 'POST':  # Tangkap data POST
        name = request.form.get('name')  # Ambil nama dari input form
    return render_template('index.html', name=name)  # Kirim nama ke template

if __name__ == '__main__':
    app.run(debug=True)
