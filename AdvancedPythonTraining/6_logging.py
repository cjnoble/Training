import logging


def some_function():

    logging.info("Function was called", extra=extData)

extData = {
    "user" : "example"
}

#config
#formatstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
formatstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%d/%m/%Y %I:%M:%S %p"

logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w", format=formatstr, datefmt=datestr) #append is default

# 5 methods
logging.debug("debug message", extra=extData) # Diagnostic info for debugging
logging.info("info message", extra=extData) # Normal operation completed ok
logging.warning("warning message", extra=extData) # Something unexpected
logging.error("error message", extra=extData) # A noraml operation didn't complete
logging.critical("critical message", extra=extData) # Program can't continue

# formatted string
logging.info(f"test {10}", extra=extData)

some_function()