import logging
a="veribule"
LOG_FORMAT = "%(user)s[%(ip)s] - %(levelname)s***%(name)s******%(message)s***%(asctime)s"
DATE_FORMAT = "%Y-%m-%d %I:%M:%S %P"
logging.basicConfig(datefmt = DATE_FORMAT,format=LOG_FORMAT,level=logging.DEBUG,filemode='w',filename="/home/tlxy/dana/tutu.txt")

logging.debug("This is debug DE {}".format(a), exc_info=True,extra={'user':'tom','ip':'47.98.53.222'})
logging.info("This is info",extra={'user':'tom','ip':'47.98.53.222'})
logging.log(logging.WARNING,'This is warning',extra={'user':'tom','ip':'47.98.53.222'})
logging.error('this is a error',extra={'user':'tom','ip':'47.98.53.222'})
logging.log(logging.CRITICAL, "This is a Critical",extra={'user':'tom','ip':'47.98.53.222'})
