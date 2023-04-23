import logging
from module import fun

LOG_FORMAT = "{levelname:<8}:{asctime}:{name}:{lineno:03d}:{msg}"

logging.basicConfig(filename="log\\log.log", filemode="w", encoding="utf-8", level=logging.NOTSET, format=LOG_FORMAT,
                    style="{")

logger = logging.getLogger(__name__)

logger.debug("Отладка")
logger.info("Информация")
logger.warning("Предупреждение")
logger.error("Ошибка")
logger.critical("Критическая ошибка")

fun()
