import configparser
import os


def getConfig():
    config = readfile()
    host = config.get("Connection", "host")
    user = config.get("Connection", "user")
    password = config.get("Connection", "password")

    oracle_path = config.get("FilePath", "oracle_path")
    rpm_path = config.get("FilePath", "rpm_path")
    return Config(Client(host, user, password), Files(oracle_path, rpm_path))


def readfile():
    config = configparser.ConfigParser()
    root_dir = os.path.abspath('.')
    config_file_path = os.path.join(root_dir, "config.ini")
    if not os.path.exists(config_file_path):
        print("配置文件不存在:" + config_file_path)
    config.read(config_file_path, encoding='utf-8')
    return config


class Config:
    def __init__(self, client, files):
        self.Client = client
        self.Files = files

    def __str__(self) -> str:
        return 'client:   {%s}\n' \
               'files:   {%s}' % (self.Client, self.Files)


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def __str__(self) -> str:
        return 'host:   %s\n' \
               'user:   %s\n' \
               'password:   %s' % (self.host, self.user, self.password)


class Files:
    def __init__(self, oracle_path, rpm_path):
        self.oracle_path = oracle_path
        self.rpm_path = rpm_path

    def __str__(self) -> str:
        return 'oracle_path:    %s\n' \
               'rpm_path:   %s' % (self.oracle_path, self.rpm_path)


print(getConfig().Client)
