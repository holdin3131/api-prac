from flask import Flask ,render_template   # 랜더 템플릿 추가
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')    # 랜더 템플릿(html 파일)



if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)