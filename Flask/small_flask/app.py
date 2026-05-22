from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/api')
def name():
    name=request.values.get('name')
    age=request.values.get('age')

    age= int(age)
    if age>18: 
        return 'welcome to the site,'+name+'!'
    else:
        return 'sorry , you are too young to visit the site'
if __name__=='__main__':
    app.run(debug=True) 

    

    
