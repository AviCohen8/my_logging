import math
import logging
# logging.basicConfig(format= '%(levelname) s  %(asctime) s message: %(message)s ', level=logging.DEBUG, datefmt='%H:%M:%S',filename='dvir.log')


l = logging.getLogger('my_logger')
handlerStrea = logging.StreamHandler()
l.setLevel(logging.DEBUG)
handlerFile = logging.FileHandler('my_logger.log')
handlerStrea.setLevel(logging.ERROR)
handlerFile.setLevel(logging.DEBUG)
l.addHandler(handlerStrea)
l.addHandler(handlerFile)
formaterFile = logging.Formatter('%(levelname) s  %(asctime) s message: %(message)s ', datefmt='%H:%M:%S')
formaterStrea = logging.Formatter('%(levelname) s %(lineno)d message: %(message)s ')
handlerStrea.setFormatter(formaterStrea)
handlerFile.setFormatter(formaterFile)


def zip_it(func):
    l.debug(f"function { func.__name__} is enetering zip_it")
    def wrapper(*args):

        l.debug(f"function{ func.__name__} is sent to wrapper with args {args}")
        [x, y] = func(*args)
        l.info(f'wrapper: func = {func.__name__} x = {x} y = {y}')
        #
        try:
            assert len(x) == len(y), "error: lists are not even"
        except AssertionError as e:
            print('uneven[0,0]')
            l.exception(e)


        return "zipped data: " + str(list(zip(x, y)))


    return wrapper


@zip_it
def log_scale(list_num):
    y = [math.log(x) for x in list_num]
    return list_num, y


@zip_it
def uneven(some_list):
    return some_list, some_list[:-1]


################## BONUS ######################
@zip_it
def filter_and_divide(*args):
    filtered = filter(lambda x: x > 10, args)
    return list(args), [y / 10 for y in filtered]


################ TEST #########################
if __name__ == "__main__":
    a = log_scale([100, 200])
    print("log scale: " + str(a))
    try:
        b = uneven([100, 200])
        print("uneven: " + str(b))
    except AssertionError as e:
        l.exception(e)



    bonus1 = filter_and_divide(234, 340, 560)
    print("bonus1: " + str(bonus1))
    try:
        bonus2 = filter_and_divide(100, 2)
        print("bonus2: " + str(bonus2))
    except AssertionError as e:
        l.exception(e)




