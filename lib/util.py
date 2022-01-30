import datetime


def print_log(log_type, log_content):
    ct = datetime.datetime.now()
    date_str = ct.strftime("%Y-%m-%d %H:%M:%S")
    print(f'[{date_str}] : {log_type} >> {log_content}')
