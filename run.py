# This is the file you run to start the server.
# It imports the 'create_app' function from our 'app' package
# and tells it to run.

from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True means the server will auto-reload
    # when you save your code.
    app.run(debug=True)