# from flask i want to import flask ,render_template,request
from flask import Flask, render_template, request,jsonify

#declare the app
app = Flask(__name__)

#start an app route
@app.route('/')
#declare a function
def main():
    return render_template('app.html')

#form submission route
@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        # start pulling out data from input form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
    #calculation IF statement  
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html',sum=sum)

        elif operation == 'subtraction':
            sum = float(num1) - float(num2)
            return render_template('app.html',sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html',sum=sum) 

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html',sum=sum) 

        else:
            return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)                
