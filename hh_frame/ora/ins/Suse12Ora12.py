# 在Suse12下安装Oracle12的的脚本
class RootConfig:
    def __init__(self, client):
        self.client = client

    # 创建文件夹
    def init_dir(self):
        dirs = ["/home/db/stage/etc/", "/u01/app/oracle/product/12.1.0/dbhome_1"]
        for str in dirs:
            cmd = 'mkdirs -p %s' % str
            self.client.exec_command(cmd)

    # 添加oracle用户和用户组
    def addOraGroup(self):
        addGroupCmdList = [
            "groupadd oinstall",
            "groupadd dba",
            "groupadd oper",
            "useradd -g oinstall -G dba,oper -d /home/oracle oracle"
        ]
        for cmd in addGroupCmdList:
            self.client.exec_command(cmd)

    # 删除oracle用户和用户组
    def delOraGroup(self):
        delGroupCmdList = [
            "userdel oracle",
            "groupdel oinstall",
            "groupdel dba",
            "groupadd oper"
        ]
        for cmd in delGroupCmdList:
            self.client.exec_command(cmd)
