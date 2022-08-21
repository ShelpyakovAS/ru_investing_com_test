import logging
import inspect


log_space = logging.getLogger('project_log')


def log(func):
    def log_save(*args, **kwargs):
        ret = func(*args, **kwargs)
        log_space.debug(f'Была вызвана функция {func.__name__} c параметрами {args}, {kwargs}. '
                        f'Вызов из модуля {func.__module__}. Из функции {inspect.stack()}')
        return ret
    return log_save