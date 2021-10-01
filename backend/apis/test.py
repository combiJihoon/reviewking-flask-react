from flask import Blueprint, render_template, request, url_for, jsonify
import pymysql
from config import db_info

bp = Blueprint('test', __name__)


@bp.route('/test', methods=['GET'])
def test():
    db = pymysql.connect(user=db_info['user'], host=db_info['host'], port=db_info['port'],
                         passwd=db_info['password'], db=db_info['database'], charset='utf8mb4')
    # cusor : 커서 생성
    cursor = db.cursor()
    # sql문 작성(데이터 read)
    sql = "SELECT * FROM reviews"
    # sql문 실행(데이터 read)
    cursor.execute(sql)
    # fetchall() : 전부 가져오기
    result = cursor.fetchall()
    # commit 및 연결 해제
    db.commit()  # 커밋은 반복할 필요 없음
    db.close()

    return jsonify(status="200", result=result)
