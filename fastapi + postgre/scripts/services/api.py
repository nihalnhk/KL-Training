# from scripts.model import  models
# num = models.num
# from db.db_setup import cursor,conn
# from main import app
#
# @app.get("/")
# def home():
#     return {"Home Page"}
#
# @app.post("/operation/{val}")
# def op(val:int,data:num):
#     if(val == 1):
#         cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
#                        (data.first, data.second,"add", (data.first + data.second)))
#
#     if (val == 2):
#         cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
#                        (data.first, data.second, "Difference", (data.second - data.first)))
#     if (val == 3):
#         cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",
#                        (data.first, data.second, "Multiplication", (data.first * data.second)))
#
#     return {"msg":"Executed Successfully"}
#
#
#
# @app.post("/addhistory")
# def push(data:num):
#     cursor.execute(f""" insert into nos(first_no,second_no,operation,ans) values(%s,%s,%s,%s)""",(data.first,data.second,data.operation,(data.first+data.second)))
#     conn.commit()
#     return {"added successfully"}
#
# @app.get("/fetchhistory")
# def fetch():
#     cursor.execute("select * from nos")
#     conn.commit()
#     data = cursor.fetchall()
#     return data
#
# @app.delete("/deletehistory")
# def delete():
#     cursor.execute("truncate table nos")
#     conn.commit()
#     return {"msg":"History cleared"}
