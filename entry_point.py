import application
from application import server

app = application.server.init()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
