#url request, route 
from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def home():
  return "welcome to home page"
@app.route('/api')
def name():
  name=request.values.get('name')
  age=request.values.get('age')
  age=int(age)
  if age>=18:
    return "welcome to the site" +name + "!"
  else:
    return "sorry , you are below 18"
if __name__=="__main__":
   app.run(debug=True)
