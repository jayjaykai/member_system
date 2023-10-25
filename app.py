# 載入 pymongo 套件
import pymongo
from bson.objectid import ObjectId
# 連線到 Mongo 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:root123@cluster0.xphs9mf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 把資料放到資料庫中
db=client.member_system

# 初始化 Flask 伺服器
from flask import *
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key="any string but secret"

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_check():
   email=request.form["email"]
   password=request.form["password"]

   con=db.user
   result=con.find_one({
       "$and":[
           {"email":email},
           {"password":password}
       ]
   })
   if(result==None):
       return redirect("/error?msg=帳號或密碼輸入錯誤！請確認！")
   else:
       session["nickname"]=result["nickname"]
       return redirect("/welcome")

@app.route("/error")
def error():
    msg=request.args.get("msg","發生錯誤，請聯繫系統管理者！")  
    return render_template("error.html", errmessage=msg)  

@app.route("/welcome")
def welcome():
    if("nickname" in session):
        title = request.args.get("title")
        content = request.args.get("content")
        
        if title and content:
            notes.append({'title': title, 'content': content})
        
        return render_template("welcome.html", notes=notes)
        # return render_template("welcome.html")
    else:
        return redirect("/")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/signup', methods=['POST'])
def register_user():
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]

    data=db.user
    result=data.find_one({
        "email":email
    })
    if(result!=None):
        return redirect("/error?msg=信箱已被註冊！")
    else:
        data.insert_one({
            "nickname":nickname,
            "email":email,
            "password":password
        })
    return redirect("/")

@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

@app.route("/founder")
def intro():
    return render_template("founder.html")

@app.route("/createnote")
def creat_note():
    return render_template("createnote.html")

notes = []
@app.route('/addnote', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    print(notes)
    notes.append({'title': title, 'content': content})
    print(notes)
    return render_template("welcome.html", notes=notes)
# 啟動網站伺服器, 可透過 port 參數指定埠號
app.run(port=3000)