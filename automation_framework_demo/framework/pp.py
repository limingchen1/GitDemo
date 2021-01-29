import codecs
import os
import configparser

pro = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(pro, 'config.ini')

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


config = configparser.ConfigParser()
path = os.path.abspath('..') + '/config/config.ini'
config.read(path)

brow = config.get('browserType', 'browserName')
print(brow)





