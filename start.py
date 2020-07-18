from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, From Flask!'

@app.route('/test',methods=['GET'])
def get():
    return jsonify({'msg':'Hello world'})

if __name__== '__main__':
    app.run()