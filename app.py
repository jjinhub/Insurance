# 라이브러리 불러오기
from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for, flash, session

# APP 생성
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

# DB 로드
con = duckdb.connect(database='./instance/members.duckdb', read_only=False)

# 클라이언트 및 서비스 설정
demo_client_id = ''
demo_client_secret = ''
public_key = ''

codef = Codef()
codef.public_key = public_key
codef.set_demo_client_info(demo_client_id, demo_client_secret)

# 홈(로그인) 페이지 라우트
@app.route('/')
def home():
    return render_template('hos_login.html')

# 회원가입 페이지
@app.route('/signup')
def signup():
    return render_template('hos_signup.html')

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
