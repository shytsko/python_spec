import logging

_logger = logging.getLogger(__name__)


def fun():
    _logger.debug("Отладка")
    _logger.info("Информация")
    _logger.warning("Предупреждение")
    _logger.error("Ошибка")
    _logger.critical("Критическая ошибка")
