from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/mysql')
def mysql_backup(name=None):
    import mysql_backup
    print("done")
    return render_template('mysql_backup.html', name=name)

@app.route('/mongodb')
def mongodb_backup(name=None):
    import mongodb_backup
    print("done")
    return render_template('mongodb_backup.html', name=name)

@app.route('/route_name')
def script_output():
    output = execute('./mongo_status')
    return render_template('mongodb_status.html',output=output)

@app.route('/mongodbstatus')
def mongodb_status():
    output = execute('./mongo_status')
    return render_template('mongodb_status.html',output=output)
 
if __name__ == '__main__':
  app.run(debug=True)