from app import app
from contacts import contacts

#cambio de tu compañero 

#rgrfgewfwewfewfewfew##
####### jjgljhgjhkgkjgjk


#nerkgnrejgn mil lineas 

app.register_blueprint(contacts)

# starting the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
