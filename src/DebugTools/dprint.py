'''Debug Print Function'''
import inspect, ntpath
import sys, time, datetime
import threading, queue, logging

# region Variables

FORMAT = '%(TIMESTAMP)s %(levelname)s [%(CALLINGFUNC)s] %(message)s'
logging.basicConfig(format=FORMAT)
LOG = logging.getLogger("debug")
LOG.setLevel(logging.DEBUG)

lLogLevels={
    50: "CRITICAL",
    40: "ERROR",
    30: "WARNING",
    20: "INFO",
    10: "DEBUG",
    0: "NOT SET"
}

class clsTermColors:
    DEBUG     = '\033[40m\033[37m'
    INFO      = '\033[40m\033[36m'
    WARNING   = '\033[47m\033[31m'
    ERROR     = '\033[41m\033[34m'
    CRITICAL  = '\033[45m\033[45m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

class clsTermPictures:
    DEBUG     = ''
    INFO      = '> '
    WARNING   = '% '
    ERROR     = '! '
    CRITICAL  = '* '
    ENDC      = ''
    BOLD      = ''
    UNDERLINE = ''

termPretty = False

# endregion

def dprint(MSG):
    __loggerMAIN(MSG, "D")

def print(MSG):
    __loggerMAIN(MSG, "I")

def logDEBUG(MSG):
    MSG = termPretty.DEBUG + str(MSG) + termPretty.ENDC
    __loggerMAIN(MSG, "D")

def logINFO(MSG):
    MSG = termPretty.INFO + str(MSG) + termPretty.ENDC
    __loggerMAIN(MSG, "I")

def logWARNING(MSG):
    MSG = termPretty.WARNING + str(MSG) + termPretty.ENDC
    __loggerMAIN(MSG, "W")

def logERROR(MSG):
    MSG = termPretty.ERROR + str(MSG) + termPretty.ENDC
    __loggerMAIN(MSG, "E")

def logCRITICAL(MSG):
    MSG = termPretty.CRITICAL + str(MSG) + termPretty.ENDC
    __loggerMAIN(MSG, "C")

def __loggerMAIN(LOGMESSAGE, LOGLEVEL):
    dtCurrent = datetime.datetime.now()
    sTimeStamp = dtCurrent.strftime("%H:%M:%S")
    sCallingFilename = ntpath.basename(inspect.stack()[2][1])
    sCallingLineNo = inspect.stack()[2][2]
    sCallingFunc = inspect.stack()[2][3]
    # sCalledFrom = sCallingFilename + "." + sCallingFunc + ":" + str(sCallingLineNo)
    sCalledFrom = sCallingFunc + ":" + str(sCallingLineNo)
    logArgs = {'CALLINGFUNC': sCalledFrom, 'TIMESTAMP': sTimeStamp }

    if LOGLEVEL == "D":
        LOG.debug(LOGMESSAGE, extra=logArgs)
    if LOGLEVEL == "I":
        LOG.info(LOGMESSAGE, extra=logArgs)
    if LOGLEVEL == "W":
        LOG.warning(LOGMESSAGE, extra=logArgs)
    if LOGLEVEL == "E":
        LOG.error(LOGMESSAGE, extra=logArgs)
    if LOGLEVEL == "C":
        LOG.critical(LOGMESSAGE, extra=logArgs)


