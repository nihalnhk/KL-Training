
from fastapi import  FastAPI
from pydantic.class_validators import Optional
from starlette.middleware.cors import CORSMiddleware

from db.db_setup import cursor,conn
from pydantic import BaseModel
from scripts.model import  models
from scripts.model.models import Users
from scripts.services import api
origins = [
"http://localhost:3000" ,
]




descr = "Values for different operation 1. Addition 2. Subtraction 3. Multiplication "

app = FastAPI(
    description=descr
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT"],
    allow_headers=["*"],
)
num = models.num



nos_dict = {"operation":" " ,1:0,2:0}

users = [];


@app.get("/")
def home():
    return users

@app.post("/store")
def add_det(v:Users):
    print(v)
    users.append(v)
    return users

@app.delete("/delete")
def deldata():
    users.clear()
    return users

@app.put("/update/{uid}")
def up_data(uid:int,v:Users):
    users[uid].name = v.name;
    users[uid].age = v.age;
    return users

@app.delete("/delete/{uid}")
def del_each_data(uid:int):
    del users[uid]
    return users





@app.post("/operation/{val}")
def op(val:int,data:num):
    if(val == 1):
        cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
                       (data.First_Number, data.Second_Number,"add", (data.First_Number + data.Second_Number)))

    if (val == 2):
        cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
                       (data.First_Number, data.Second_Number, "Difference", (data.Second_Number - data.First_Number)))
    if (val == 3):
        cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
                       (data.First_Number, data.Second_Number, "Multiplication", (data.First_Number * data.Second_Number)))

    return {"msg":"Executed Successfully"}



@app.post("/addhistory")
def push(data:num):
    cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",(data.first,data.second,data.operation,(data.first+data.second)))
    conn.commit()
    return {"added successfully"}


@app.get("/fetchhistory")
def fetch():
    cursor.execute("select * from nos")
    conn.commit()
    data = cursor.fetchall()
    return data


@app.delete("/deletehistory")
def delete():
    cursor.execute("truncate table nos")
    conn.commit()
    return {"msg":"History cleared"}

