#      Import modules
from django.shortcuts import render
from django.http import HttpResponse

#?      Import my modules

from .mod.Mutils1 import (
    
    RequestForServersDefualtInfo, 
        ServersDefualtInfo,

    RequestForServersExtendedInfo, #TODO:  <--- Реализовать
        ServersExtendedInfo
    )


def index(request):
    RequestForServersDefualtInfo()
    data = {"info":ServersDefualtInfo, "DorE":False}
    return render(request=request, template_name="index.html", context=data)

def SIndex(request, id, DorE):
    if DorE == "Default":
        RequestForServersDefualtInfo()
        data = {"info":ServersDefualtInfo[id]}
        return render(request=request, template_name="Server.html", context=data)  
    elif DorE == "Extended":
        RequestForServersExtendedInfo()
        data = {"info":ServersExtendedInfo[id]}
        return render(request=request, template_name="EServer.html", context=data) 
    else:
        raise Exception(f"{DorE} не равен Defualt и Extended")
