# from overrides import override
from typing import NoReturn
from requests import get
from functools import lru_cache



class MessageBox():
    """
    from time import localtime\n
    Time = f"{localtime().tm_hour}:{localtime().tm_min}:{localtime().tm_sec}"\n
    MsgBox = MessageBox() \n
    MsgBox.CreateMessageBox(None, f"{Time} - Server is start", "Server Info", 0x1, 0x10, 0x0, 0x0, 0x0)
    """

    
    from ctypes import c_uint, c_char, CDLL

    def __init__(self) -> None:
        self.lib = self.CDLL(r"C:\Users\soho66\Desktop\PythonProjects\Django\Django_GetServersInfo.Dynast\django1\Application1\mod\DllProj1.dll")

    def CreateMessageBox(self, hWnd:None, lpText:c_char, lpCaption:c_char,
            uType1:c_uint,
            uType2:c_uint,
            uType3:c_uint,
            uType4:c_uint,
            uType5:c_uint): 
        self.lib.MsBox(hWnd,lpText,lpCaption, uType1, uType2, uType3, uType4, uType5)    

request = get("https://announcement-amsterdam-0-alpaca.dynast.cloud/all")

if request.status_code == 200:    
    data = request.json()
else:
    ErorrBox = MessageBox()
    ErorrBox.CreateMessageBox(hWnd=None,lpText=f"ConnectionError, status_code = {request.status_code}", lpCaption="Error",uType1=0x0,uType2=0x0, uType3=0x0, uType4=0x10, uType5=0x0)

ServersDefualtInfo = {}
@lru_cache(maxsize=None)
def RequestForServersDefualtInfo() -> NoReturn:
        for index, server in enumerate(data["servers"], start=1):
            try:
                events_NAME = server["events"][0]["kind"]["type"]
                private = server["private"]           
                label = server["label"]
                ServersDefualtInfo.setdefault(index,
                                            {
                                            "label": label, # server["label"] -> label
                                            "region": server["region"],
                                            "clientC": server["client_count"],
                                            "connectionsL": server["connections_limit"],
                                            "TopPN": server["top_player_name"],
                                            "TopPS": server["top_player_score"],
                                            "TopPL": server["top_player_level"],
                                            "event": events_NAME,
                                            "version": server["version"],
                                            "private_TorF": private,
                                            },
                                    )
            except IndexError: # Если сервер приватный то у него нету ивентов.
                events_NAME = None      
            finally:
                    private = server["private"]  
                    label = server["label"]
                    ServersDefualtInfo.setdefault(index,
                                                {
                                                "label": label, # server["label"] -> label
                                                "region": server["region"],
                                                "clientC": server["client_count"],
                                                "connectionsL": server["connections_limit"],
                                                "TopPN": server["top_player_name"],
                                                "TopPS": server["top_player_score"],
                                                "TopPL": server["top_player_level"],
                                                "event": events_NAME,
                                                "version": server["version"],
                                                "private_TorF": private,
                                                },
                                        )
        return 0
        
ServersExtendedInfo = {}
def RequestForServersExtendedInfo() -> NoReturn:
        for index, server in enumerate(data["servers"], start=1):
            try:
                events_NAME = server["events"][0]["kind"]["type"]
                private = server["private"]           
                label = server["label"]
                ServersExtendedInfo.setdefault(index,
                                            {
                                                #?      Defualt
                                            "label": label,
                                            "region": server["region"],
                                            "clientC": server["client_count"],
                                            "connectionsL": server["connections_limit"],
                                            "TopPN": server["top_player_name"],
                                            "TopPS": server["top_player_score"],
                                            "TopPL": server["top_player_level"],
                                            "event": events_NAME,
                                            "version": server["version"],
                                            "private_TorF": private,
                                                #?       Extended
                                            "sslPort": server["ssl_port"],
                                            "sslPPort": server["ssl_ping_port"],
                                            "port": server["port"],
                                            "PPort": server["ping_port"],
                                            "ip": server["ip"],
                                            "PKey": server["peer_key"],
                                            "map": server["map"],
                                            "GM": server["game_mode"],
                                            "CM": server["custom_mode"],
                                            "Lavg": server["load_avg"],
                                            "Lmax": server["load_max"],
                                            "backend": server["backend"],
                                            "frameDrop": server["frame_drop"],
                                            "ServerTime": server["server_time"],
                                            "ServerLifetime": server["lifetime"],
                                            "Lmax": server["load_max"],
                                            "AllEvents": server["events"],
                                            "NewIo": server["new_io"],
                                            "PubsubConn": server["pubsub_connected"],
                                            },
                                    )
            except IndexError: # Если сервер приватный то у него нету ивентов.
                events_NAME = None      
            finally:
                    private = server["private"]  
                    label = server["label"]
                    ServersExtendedInfo.setdefault(index,
                                                {
                                                "label": label,
                                                "region": server["region"],
                                                "clientC": server["client_count"],
                                                "connectionsL": server["connections_limit"],
                                                "TopPN": server["top_player_name"],
                                                "TopPS": server["top_player_score"],
                                                "TopPL": server["top_player_level"],
                                                "event": events_NAME,
                                                "version": server["version"],
                                                "private_TorF": private,

                                                "sslPort": server["ssl_port"],
                                                "sslPPort": server["ssl_ping_port"],
                                                "port": server["port"],
                                                "PPort": server["ping_port"],
                                                "ip": server["ip"],
                                                "PKey": server["peer_key"],
                                                "map": server["map"],
                                                "GM": server["game_mode"],
                                                "CM": server["custom_mode"],
                                                "Lavg": server["load_avg"],
                                                "Lmax": server["load_max"],
                                                "backend": server["backend"],
                                                "frameDrop": server["frame_drop"],
                                                "ServerTime": server["server_time"],
                                                "ServerLifetime": server["lifetime"],
                                                "AllEvents": server["events"],
                                                "NewIo": server["new_io"],
                                                "PubsubConn": server["pubsub_connected"],
                                                },
                                        )
        return 0