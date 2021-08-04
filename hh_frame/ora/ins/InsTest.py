import paramiko
from hh_frame.ora.config import config
from hh_frame.ora.ins.Suse12Ora12 import RootConfig

config = config.getConfig()

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(config.Client.host, username=config.Client.user, password=config.Client.password)
cfg = RootConfig(client)
cfg.addOraGroup()
# TODO 其他安装
client.close()
