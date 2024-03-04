# 라이브러리 불러오기
from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for, flash, session

# APP 생성
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

# 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
