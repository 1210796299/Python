import paramiko
from hh_frame.ora.ins.Suse12Ora12 import RootConfig

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('192.168.23.13', username='root', password='123456')
cfg = RootConfig(client)
#TODO 其他卸载
cfg.delOraGruop()
client.close()