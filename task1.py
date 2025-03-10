import logging

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Формат сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для сообщений уровня DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

# Обработчик для сообщений уровня WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)
logger.addHandler(warnings_errors_handler)

# Логирование сообщений различных уровней
logger.debug('Сообщение уровня DEBUG.')
logger.info('Сообщение уровня INFO.')
logger.warning('Сообщение уровня WARNING.')
logger.error('Сообщение уровня ERROR.')
logger.critical('Сообщение уровня CRITICAL.')
