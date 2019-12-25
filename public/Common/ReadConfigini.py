import configparser
import os
import codecs


class ReadConfigini(object):
    '''

    '''
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def getConfigValue(self, section, name):
        value = self.cf.get(section, name)
        return value


if __name__ == '__main__':
    #  获取当前文件运行路径
    file_path = os.path.split(os.path.realpath(__file__))[0]
    print(file_path)
    read_config = ReadConfigini(os.path.join(file_path, 'Config.ini'))
    print(read_config)
    value = read_config.getConfigValue("project", "project")
    print(value)
