import paramiko
from hh_frame.ora.ins.Suse12Ora12 import RootConfig

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('192.168.23.13', username='root', password='123456')
cfg = RootConfig(client)
cfg.addOraGruop()
#TODO 其他安装
client.close()