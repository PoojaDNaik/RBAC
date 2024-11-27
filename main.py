import os
from typing import Any, List, Dict
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from collections import defaultdict
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from crud import checkForValidLoginAdmin, checkForValidLoginUser, createUser, getUserDetails, getAdminIndividualDetail, getUserIndividualDetail, updateUser, addAdmin, removeUser, addUser, addAdmin, deleteUser, updatePassword

# templates = Jinja2Templates(directory="templates")
templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "templates"))

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/forgotPassword", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("forgotPassword.html", {"request": request})

@app.get("/admin",response_class=HTMLResponse)
async def getRegFile(request:Request):
    return templates.TemplateResponse("admin.html",{"request": request})

@app.post("/login")
async def validateLogin(body: Dict[Any, Any]):
    admin = checkForValidLoginAdmin(body["email"], body["password"])
    if admin: 
        return {"success": True, "user_type": "admin", "user": admin[0]}
    
    else :
        user = checkForValidLoginUser(body["email"], body["password"])
        if user:  
            return {"success": True, "user_type": "user", "user": user[0]}
    
    return {"success": False, "message": "Invalid email or password"}

@app.post("/forgotPassword")
async def forgotPassword(body: Dict[Any,Any]):
    status = updatePassword(body['email'],body['password'])
    if(status == True):
        return {"success" : True}
    else:
        return {"success" : False}

@app.get("/user",response_class=HTMLResponse)
async def getRegFile(request:Request):
    return templates.TemplateResponse("user.html",{"request": request})

@app.get("/register",response_class=HTMLResponse)
async def getRegFile(request:Request):
    return templates.TemplateResponse("register.html",{"request": request})

@app.post("/register")
async def validateReg(body: Dict[Any, Any]):
    user = createUser(body["email"],body["password"])
    if(user == False):
        return {"success":False}
    else:
        return {"success":True,"id":user[0]}
    
@app.post("/getDetail-forAdmin")
async def getDetailsEndpoint(body: Dict[Any, Any]):
    users = getUserDetails() 
    admin = getAdminIndividualDetail(body['email'])
    return {"users": users, "admin": admin}

    
@app.post("/getDetail-forUser")
async def getUserDetailsEndpoint(body: Dict[Any, Any]):
    user = getUserIndividualDetail(body['email'])
    if user == None:
        return {'success' : False}
    else:
        return {"user": user }

@app.post("/updateUser")
async def updateUserDetails(body:Dict[Any,Any]):
    updateUser(body['id'],body['email'],body['password'],body['role'],body['status'])
    return {"success" : True}

@app.post("/addAdmin")
async def addNewAdmin(body:Dict[Any , Any]):
    addAdmin(body['email'],body['password'])
    removeUser(body['id'])
    return {"success" : True}

@app.post("/addUser")
async def addNewUSer(body:Dict[Any,Any]):
    if body['role'] == 'user':
        addUser(body['email'],body['password'],body['role'])
    else:
        addAdmin(body['email'],body['password'])
    return {"success" : True}

@app.post("/deleteUser")
async def deleteSelectedUser(body : Dict[Any, Any]):
    deleteUser(body['id'])
    return {'success' : True}