from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/data_access')
def data_access():
  return render_template('data_access.html')
 
@app.route('/data_tools')
def data_tools():
  return render_template('data_tools.html')

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/maps')
def maps():
  return render_template('maps.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/research')
def research():
  return render_template('research.html')

@app.route('/system')
def system():
  return render_template('system.html')

if __name__ == '__main__':
  app.run(debug=True)
