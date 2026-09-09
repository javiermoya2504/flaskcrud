from app import app
from contacts import contacts

#cambio de juanito perez
##323rq4wr34wr43r34r2342343
"#"#!"#123123"
#####rergregergreg 1000 lineas


app.register_blueprint(contacts)

# starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
