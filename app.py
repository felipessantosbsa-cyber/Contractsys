from flask import Flask, render_template, request
from database import create_tables, insert_contract, get_all_contracts
app = Flask(__name__)

@app.route("/")
def way_route():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        client = request.form.get("client")
        local = request.form.get("local")
        value = request.form.get("value")
        entry_date = request.form.get("entry_date")
        email_user = request.form.get("email_user")

        print(f"Cliente: {client}")

        insert_contract(client, local, value, entry_date, email_user)
        return("contrato cadastrado com sucesso!")
    
    return render_template("cadastrar.html")



if __name__ == "__main__":
    create_tables()
    app.run(debug=True)