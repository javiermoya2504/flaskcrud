from app import app
from contacts import contacts

#ewfwefwefewqfweqfwef

app.register_blueprint(contacts)

# starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
