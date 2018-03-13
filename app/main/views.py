from app.main import app_main
from flask import render_template, request
from app import db
from sqlalchemy.orm import mapper
import os
import time
import json

@app_main.route('/index' , methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app_main.route('/login', methods=['POST','GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    from ..models import user
    user = db.session.query(user.User).filter_by(username=username, password=password).first()
    if(user):
        return json.dumps({'legal':True})
    else:
        return json.dumps({'legal':False})


@app_main.route('/getMenu' , methods=['POST','GET'])
def getMenu():
    from ..models import menu
    menus = db.session.query(menu.Menu).all()
    menusDict = anyRow2dict(menus)

    menuTree = makeMenuTreeNode(menusDict)

    return json.dumps(menuTree)
@app_main.route('/getChildMenu' , methods=['POST','GET'])
def getChildMenu():
    menuId = request.form.get('node')
    from ..models import menu
    menus = db.session.query(menu.Menu).filter_by(top_id=menuId).all()
    menusDict = anyRow2dict(menus)
    return json.dumps(menusDict)

@app_main.route('/getUserInfo' , methods=['POST','GET'])
def getUserInfo():
    username = request.form.get('username')
    from ..models import user
    userinfo = db.session.query(user.User).filter_by(username=username).one()
    print userinfo.username
    userDict = oneRow2dict(userinfo)
    return json.dumps(userDict)

@app_main.route('/getGameById' , methods=['POST','GET'])
def getGameById():
    id = request.form.get('id')
    from ..models import game
    gameInfo = db.session.query(game.Game).filter_by(id=id).one()
    gameDict = oneRow2dict(gameInfo)
    return json.dumps(gameDict)

@app_main.route('/getLogInfo' , methods=['POST','GET'])
def getLogInfo():
    '''
    gameId = request.form.get('gameId')
    Ymd = request.form.get('dateTime')
    '''
    gameId = 9
    Ymd = '20180213'
    from ..auth.logInfo import LogInfo
    logInfo = LogInfo(gameId ,Ymd, 'MoneyFlow')
    logInfo.runShell()


@app_main.route('/getCoreUser' , methods=['POST','GET'])
def getCoreUser():
    y = request.form.get('Y')
    m = request.form.get('M')
    d = request.form.get('D')
    print y
    print m
    print d
    Ymd = y+'-'+m+'-'+d
    t_unix = int(time.mktime(time.strptime(Ymd,'%Y-%m-%d')))

    from ..models.coreUser import CoreUser
    from sqlalchemy import func

    coreInfo = db.session.query(func.sum(CoreUser.num), func.substr(CoreUser.groupid, 1, 4) , CoreUser.created).filter(CoreUser.created>=t_unix).group_by(func.substr(CoreUser.groupid, 1, 4) , CoreUser.created).order_by(func.substr(CoreUser.groupid, 1, 4) , CoreUser.created).all()
    arr = []
    for list in coreInfo:
        tmp = (str(list[0]) , list[1]+'0000', list[2])
        arr.append(tmp)
    print arr
    return json.dumps(arr)


def makeMenuTreeNode(menusDict):
    node_top = []
    childArr = []
    for node in menusDict:
        if(node['top_id'] == 0):
            node_top.append({0:node})
        else:
            childArr.append(node)

    pos = 0
    for nodeChild in childArr:
        if '1' in node_top[nodeChild['top_id']]:
            pos+=1
            node_top[nodeChild['top_id']]['1'] = dict(node_top[nodeChild['top_id']]['1'] , **{pos:nodeChild})
        else:
            pos = 0
            node_top[nodeChild['top_id']]['1'] = {pos : nodeChild}

    for nodeChild in node_top:
        print nodeChild

    return node_top



def anyRow2dict(anyrow):
    allNode = []
    for row in anyrow:
        node = {}
        for column in row.__table__.columns:
            node[column.name] = getattr(row,column.name)
        allNode.append(node)
    return allNode


def oneRow2dict(oneRow):
    node = {}
    for row in oneRow.__table__.columns:
        node[row.name] = getattr(oneRow,row.name)
    return node

#getCoreUser()