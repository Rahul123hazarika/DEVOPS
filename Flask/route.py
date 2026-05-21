import flask from Flask
app=Flask(__name__)
@app.route('/'): #route
def home():
  return 'welcome'
@app.route('/second'): #route
  return "hi !"
if __name__=='__main__':
  app.run(debug=True)
