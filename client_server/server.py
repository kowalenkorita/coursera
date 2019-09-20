import asyncio

class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def process_data(data):
    com, metric = data.split(' ', 1)

    if com == 'get':
        return get(metric)
    elif com == 'put':
        return put(metric)
    else:
        return 'error\nwrong command\n\n'

d = {}
result = 'ok\n\n'

def put(data):
    key, value, timestamp  = data.split()

    if key in d:
        d[key].update({timestamp: value})
    else:
        d[key] = {}
        d[key].update({timestamp: value})

    return result


def get(data):
    key = data.strip()
    res = 'ok\n'
    if key == '*':
        for k, value in d.items():
            for timestamp in value:
                res += ('{} {} {}\n').format(k, value[timestamp], timestamp)
        res += '\n'
        return res
    else:
        value = d.get(key)
        if value:
            for timestamp in value:
                res += ('{} {} {}\n').format(key, value[timestamp], timestamp)
            res += '\n'
            return res
        else:
            return result
    


# loop = asyncio.get_event_loop()
# coro = loop.create_server(
#     ClientServerProtocol,
#     '127.0.0.1', 8888
# )

# run_server( "127.0.0.1", 8888 )