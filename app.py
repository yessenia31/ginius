from flask import Flask, render_template

app = Flask(__name__)




@app.route("/prueba")
def prueba ():
    return render_template("homepage.html")




if __name__ == "__main__":
    app.run(debug=True) #ejecuta la aplicacion Flask facilmente desde la ternimal.

