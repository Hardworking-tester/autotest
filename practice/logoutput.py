# encoding:utf-8

from selenium import webdriver
import unittest,logging,time
def log1():

    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    filehandle=logging.FileHandler("E:\\wwg\\log.txt")
    filehandle.setLevel(logging.INFO)
    formatter=logging.Formatter("%(asctime)s: %(message)s","%Y年%M月%d日 %H:%M:%S")
    filehandle.setFormatter(formatter)
    logger.addHandler(filehandle)
    logger.info("wwg")
def main():
    log1()

if __name__=="__main__":
    main()


