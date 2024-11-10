#      Import modules
from django.shortcuts import render
from django.http import HttpResponse

#     Don`t use this modules
# from typing import NoReturn
# import requests
# from functools import lru_cache
# from django.template.response import TemplateResponse
# from Dll_Python.main2 import MessageBox

#?      Import my modules

# import sys
# sys.path.append(r"django1\Application1\mod\Mutils1.py")
from .mod.Mutils1 import (
            MessageBox,

    RequestForServersDefualtInfo, 
        ServersDefualtInfo,

    RequestForServersExtendedInfo, #TODO:  <--- Реализовать
        ServersExtendedInfo
    )

# MsgBox = MessageBox()
RequestForServersDefualtInfo()
#Servers.ServersExtendedInfo()

def index(request):
    data = {"info":ServersDefualtInfo, "DorE":False}
    return render(request,"index.html", context=data)  #! Законченно!

def SIndex(request, id, DorE):
    if DorE == "Defualt":
        data = {"info":ServersDefualtInfo[id]}
        # MsgBox.CreateMessageBox(None, f"Сервер найден, продолжить?", "Server Info", 0x0, 0x40, 0x0, 0x0, 0x0)
        #TODO: сделать RequestForServersExtendedInfo, добавить визуализацию и обработку расширенной информации
        return render(request=request, template_name="Server.html", context=data)  
    elif DorE == "Extended":
        data = {"info":ServersExtendedInfo[id]}
        # MsgBox.CreateMessageBox(None, f"Сервер найден, продолжить?", "Server Info", 0x0, 0x40, 0x0, 0x0, 0x0)
        #TODO: сделать RequestForServersExtendedInfo, добавить визуализацию и обработку расширенной информации
        return render(request=request, template_name="EServer.html", context=data) 
    else:
        raise Exception(f"{DorE} не равен Defualt и Extended")

def about(request):
    return HttpResponse("""
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        
                        <h1 align=center>About!</h1>
                        
                        """)