import logging
import os
import sys
import logging.handlers


format_log = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'project_log.log')

client_handler = logging.StreamHandler(sys.stderr)
client_handler.setFormatter(format_log)
client_handler.setLevel(logging.ERROR)

log_file = logging.FileHandler(PATH, encoding='utf8')
log_file.setFormatter(format_log)

log = logging.getLogger('project_log')
log.addHandler(client_handler)
log.addHandler(log_file)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    log.critical('Критическая ошибка')
    log.error('Ошибка')
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
