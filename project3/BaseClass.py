import logging


class BaseClass:
    def getLogger(self, testName):
        logger = logging.getLogger(testName)
        fileHandler = logging.FileHandler("logfile_report.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s %(funcName)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
