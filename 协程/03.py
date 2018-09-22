from collections import namedtuple
ResClass = namedtuple('Res', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        if term is None:
            break

        total += term
        count += 1
        average = total / count

    return ResClass(count, average)

def grouper(storages, key):
    while True:
        # 获取averager()返回的值
        storages[key] = yield from averager()

def client():
    process_data = {
        'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }

    storages = {}
    for k, v in process_data.items():
        coroutine = grouper(storages, k)
        # 预激协程
        next(coroutine)
        # 发送数据到协程
        for dt in v:
            coroutine.send(dt)
        # 终止协程
        coroutine.send(None)
    print(storages)

if __name__ == '__main__':
    client()