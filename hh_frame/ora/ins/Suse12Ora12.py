# 在Suse12下安装Oracle12的的脚本
class RootConfig:
    def __init__(self, client):
        self.client = client
    
    def addOraGruop(self):
        addGroupCmdList = [
            "groupadd oinstall",
            "groupadd dba",
            "groupadd oper",
            "useradd -g oinstall -G dba,oper -d /home/oracle oracle"
        ]
        for cmd in addGroupCmdList:
            self.client.exec_command(cmd)

    def delOraGruop(self):
        delGroupCmdList = [
            "userdel oracle",
            "groupdel oinstall",
            "groupdel dba",
            "groupadd oper"
        ]
        for cmd in delGroupCmdList:
            self.client.exec_command(cmd)