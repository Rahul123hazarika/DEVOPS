from flask import Flask, render_template, request
from datetime import datetime 
app=Flask(__name__)
@app.route('/')
def home():
    day_of_week=datetime.now().strftime('%A') 
    #.strftime('%A'): This is a method called "string format time." It takes the datetime object and formats it into a human-readable string based on the code you provide inside the parentheses.
    # %A: This specific directive tells Python to return the full name of the weekday (e.g., Sunday).
    current_time=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html',day_of_week=day_of_week,current_time=current_time)

@app.route('/time')
def time():
    current_time=datetime.now().strftime('%H:%M:%S') #here H: hour , M: minute , S: second
    return current_time
if __name__=='__main__':
    app.run(debug=True)
     
