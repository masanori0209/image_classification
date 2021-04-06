import bottle
import routes

app = routes.app

if __name__ == '__main__':
    bottle.run(
        host='0.0.0.0',
        app=app,
        port=9000,
        reloader=True,
        debug=True
    )