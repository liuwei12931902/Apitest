import time
import os
import logging
from Config import GlobalConfig

"""
工程使用需求：
1-不同日志名称
2-打印同时在控制台，也有文件
3-灵活控制等级
"""


class RunLogger(object):

    def debug_log(self, logger_name='DEBUG-LOG', level=logging.DEBUG):
        # 创建 logger对象
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)  # 添加等级

        # 创建控制台 console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 创建文件 handler
        log_file = os.path.join(GlobalConfig.log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        fh = logging.FileHandler(filename=log_file, encoding='utf-8')

        # 创建 formatter
        formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

        # 添加 formatter
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 把 ch， fh 添加到 logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger


if __name__ == '__main__':
    logger = RunLogger()
    logger.debug_log()
