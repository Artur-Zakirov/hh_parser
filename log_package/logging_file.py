import datetime


def logger(path):

    def __logger(old_function):

        def new_function(*args, **kwargs):
            nonlocal path
            stat = datetime.datetime.now().strftime('%d.%m.%Y %H:%m')
            func_name = old_function.__name__
            arguments = f'{args}, {kwargs}'
            response = old_function(*args, **kwargs)
            log = f'Время запуска функции: {stat}\n' \
                  f'Имя функции: {func_name}\n' \
                  f'Переданные аргументы: {arguments}\n' \
                  f'Возвращаемое значение: {response}\n'
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log)
            return response

        return new_function

    return __logger