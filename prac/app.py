from flask import Flask
app = Flask(__name__)

@app.route('/')               #홈페이지 메인 localhost:5000
def home():
   return 'This is Home!'

@app.route('/mypage')         #' /mypage ' 로 수정
def mypage():                 # mypage 로 수정
   return 'mypage 입니다'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)