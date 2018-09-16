from libroute import libroute
# Import main middleware thing
from middleware import main
#libroute.get_routes(None, None, None)

if __name__ == '__main__':
    main.app.run(host= '0.0.0.0',port = 8000)
    # Start the server
    pass
