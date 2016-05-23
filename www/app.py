from flask import Flask, request, session, abort, jsonify, redirect, url_for, abort, render_template, flash
from model import User, Questionnaire, Topic, next_id, Menu, Vote
from database import db_session
from datetime import datetime
import uuid

app = Flask(__name__)
#SECRET_KEY必须要设置，否则使用session会出错
SECRET_KEY = 'development key'
# from_object() 会查看给定的对象（如果该对象是一个字符串就会 直接导入它），搜索对象中所有变量名均为大字字母的变量。
# 在我们的应用中，已经将配 置写在前面了。你可以把这些配置放到一个独立的文件中。
# from_object() 一行替换为:
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
# 这样做就可以设置一个 FLASKR_SETTINGS 的环境变量来指定一个配置文件，并 根据该文件来重载缺省的配置。 
# silent 开关的作用是告诉 Flask 如果没有这个环境变量 不要报错。

app.config.from_object(__name__)
'''
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = {'email':'Email address', 'password':'Password', 'login':False}
    if request.method == 'POST':
        u = User.query.filter(User.email == request.form['email']).first()
        if not u:
            message['email'] = 'Invalid email'
        elif request.form['password'] != u.passwd:
            message['password'] = 'Invalid password'
        else:
            session['logged_in'] = True
            message['login'] = True
            return redirect(url_for('get'))
    return render_template('login.html', message=message)
'''
@app.route('/question', methods=['GET'])
def question():
    now = datetime.now()
    # 返回当天的菜单
    data = {"menus":[m.to_dict() for m in Menu.query.filter(Menu.date == now.strftime("%Y-%m-%d")).all()]}
    return render_template('question.html', data=data)
    #return str(data)

@app.route('/menu', methods=['GET'])
def menu():
    return render_template('menu.html')

@app.route('/api/addmenu', methods=['POST'])
def add_menu():
    date = request.form['date']
    content = request.form['content']
    menu = Menu(id=uuid.uuid4().hex,content=content, date=date)
    dbs = db_session
    dbs.add(menu)
    dbs.commit()
    dbs.close()
    return redirect(url_for('menu'))


@app.route('/api/vote', methods=['POST'])
def vote():
    menu_id = request.form['id']
    value = request.form['value']
    vote = Vote(id=next_id(),menu_id=menu_id,value=value)
    socre = []
    dbs = db_session
    dbs.add(vote)
    dbs.commit()
    # data = {"votes":[v.to_dict() for v in Vote.query.filter(Vote.menu_id == menu_id).all()]}
    for v in Vote.query.filter(Vote.menu_id == menu_id).all():
        socre.append(v.value)
    dbs.close()
    return str(int(sum(socre)/len(socre)*100))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
