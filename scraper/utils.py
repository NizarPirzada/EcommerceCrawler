import json
import random
import time

import win32api
import datetime
import pytz
from fake_useragent import UserAgent
from . import settings

time_tuple = (
    2012,  # Year
    9,  # Month
    6,  # Day
    0,  # Hour
    38,  # Minute
    0,  # Second
    0,  # Millisecond
)


def _win_set_time(time_zone):

    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    timezone_pytz = pytz.timezone(time_zone)
    timezone_time = datetime.datetime.now(timezone_pytz)
    # timezone_time = dt.replace(tzinfo=timezone_pytz)

    timezone_time_tuple = tuple(timezone_time.strftime("%Y %m %d %H %M %S %f").split())
    # dayOfWeek = datetime.datetime(utc_time_tuple).isocalendar()[2]
    time_tuple = (
        timezone_time_tuple[:2]
        + tuple([timezone_time.weekday()])
        + timezone_time_tuple[2:]
    )
    time_list = [int(i) for i in time_tuple]
    win32api.SetSystemTime(2022, 9, 5, 3, 13, 22, 12, 13)


def acp_api_send_request(driver, message_type, data=None):
    if data is None:
        data = {}
    message = {
        "receiver": "antiCaptchaPlugin",  # this receiver has to be always set as antiCaptchaPlugin
        "type": message_type,  # request type, for example setOptions
        # merge with additional data
        **data,
    }
    # run JS code in the web page context
    # precisely we send a standard window.postMessage method
    return driver.execute_script(
        """
    return window.postMessage({});
    """.format(
            json.dumps(message)
        )
    )


def get_random_proxy():
    proxies_list = settings.PROXY_LIST
    proxy = proxies_list[random.randint(0, len(proxies_list) - 1)]
    proxy = "185.189.39.242:8800"
    print("proxy:", proxy)
    return proxy


def get_user_agent():
    return UserAgent().random


def get_random_number(min=10, max=20):
    return random.randint(min, max)


def random_sleep(min=10, max=20):
    time.sleep(random.randint(min, max))


def convert_class_objects_to_list_dic(objects):
    return [obj.__dict__["_values"] for obj in objects]


def slug_to_name(slug):
    return slug.replace("-", " ").title().strip()


def clean_text(text=""):
    filter_sen = ''.join([chr(i) for i in range(1, 32)])
    return text.translate(str.maketrans('', '', filter_sen)).strip()
