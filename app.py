from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "안녕하세요 제 이름은 송수민 입니다. 만나서 반갑습니다."


if __name__ =='__main__':
    app.run()
    
