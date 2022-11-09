from time import localtime

day_str = f"{localtime().tm_mday}-{localtime().tm_mon}-{localtime().tm_year}"

def make_log(log: str, error: str=''):
    with open(f'logs/{day_str}.log', 'a') as log_file:
        log_file.write(str(log) + str(error) + '\n')