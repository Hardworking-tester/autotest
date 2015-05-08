# encoding:utf-8
import logging
def resultLog():
    log=logging.getLogger("wwg")
    log.setLevel(logging.INFO)
    filehandler=logging.FileHandler("F:\\resultlog\\resultlog.txt")
    filehandler.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s: %(message)s","%Y年%M月%d日 %H:%M:%S")
    filehandler.setFormatter(formatter)
    log.addHandler(filehandler)
    return log



