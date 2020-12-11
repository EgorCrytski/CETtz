from flask import Flask
import sys
import requests


app = Flask(__name__)
remote_address = sys.argv[1]
my_port = sys.argv[2]
threads = sys.argv[3]


@app.route('/isavailable')
def hello():
    return 'Hello'

@app.before_first_request
def ppp():
    print('IT WORKS')

@app.route('/task/add')
def add_task():
    return 'task added'


def register_unit(host_ip_port, my_port, threads):
    while True:
        try:
            response = requests.post(f'http://{host_ip_port}/api/v1/srv/unit/add',
                                 json={'port': my_port, 'threads': threads})
            if response.status_code == 201:
                break
        except:
            print('Host is down. Reconnecting.')


with app.app_context():
    register_unit(remote_address, my_port, threads)
    pass


def run():
    app.run(port=my_port)


if __name__ == "__main__":
    run()
