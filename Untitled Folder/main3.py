import logging
import functions2

logging.basicConfig(
    filename="test.log",
    level=logging.INFO
)

logger=logging.getLogger("main_no_byeol")
logger.setLevel(logging.INFO)

logger.debug("디버깅")
logger.info("정보확인")
logger.warning("경고")

functions2.log_waring()