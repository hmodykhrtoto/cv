# S2_server.py
from flask import Flask, render_template , request , redirect
from flask_mail import Mail, Message



app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'Mohamed Khartoutu'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# Read CSV and generate HTML table
@app.route("/" ,  methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Name = request.form.get('name')
        Email = request.form.get('name')
        Msg = request.form.get('name')

        msg = Message(Name, Email, 'hkhrtoto@gmail.com')
        msg.body = Msg
        mail.send(msg)
        return redirect('/')
    return render_template("index.html")

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
