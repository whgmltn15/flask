from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template('intro_2.html')

@app.route('/namgil', methods=['POST'])
def mul():
    mul = request.form["number"]
    mul = int(mul)
    return "{} * {} = {}".format(mul, 1, mul*1)

if __name__ == '__main__':
    app.run()