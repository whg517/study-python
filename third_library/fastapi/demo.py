from uvicorn import run

from third_library.fastapi.server import create_app
from multiprocessing import Process


def start_server():
    app = create_app()
    run(
        app
    )


if __name__ == '__main__':
    p = Process(target=start_server, args=())
    p.start()
    print('start')
    # p.join()
    # print('join')
