import logging as l
# import div as d
from datetime import datetime

# d.print_1_to_10()
now = datetime.now()
_time = now.strftime("%H%M%S")
print(_time)

# logger = l.getLogger(__name__)
logger = l.getLogger('avi')
# logger.setLevel(l.DEBUG)
handler1 = l.FileHandler('my_file.log')
handler = l.StreamHandler()
handler.setLevel(l.CRITICAL)
handler1.setLevel(l.DEBUG)
logger.addHandler(handler1)
formater = l.Formatter(logger)


logger.addHandler(handler)

logger.warning('Protocol problem: %s', 'connection reset')


def times(x, y):
    l.warning('add: {} * {} = {}'.format(x, y, x * y))
    l.debug('hi')


def divided(x, y):
    l.warning(x / y)


times(5, 6)
divided(80, 9)
