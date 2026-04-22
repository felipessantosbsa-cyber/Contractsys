from flask import Flask, render_template, request, send_file
from database import create_tables, insert_contract, get_all_contracts, DATABASE_NAME
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

@app.route("/")
def way_route():
    return render_template("index.html")

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        client = request.form.get("client")
        cpf_client = request.form.get("cpf_client")
        local = request.form.get("local")
        cep = request.form.get("cep")
        rent_value = request.form.get("rent_value")
        entry_date = request.form.get("entry_date")
        email_user = request.form.get("email_user")
        file_upload = request.files.get("file_upload")

        file_path = None
        if file_upload and file_upload.filename != "":
            filename = file_upload.filename

            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file_upload.save(filepath)
            
            file_path = filepath
            print(f"arquivo salvo em >>> {filepath}")

        print(f"Cliente: {client}")

        insert_contract(client, cpf_client, local, cep, rent_value, entry_date, email_user, file_path)
        return("contrato cadastrado com sucesso!")
    
    return render_template("cadastrar.html")

@app.route("/listar")
def listar():
    contracts = get_all_contracts()
    return render_template("listar.html", contracts=contracts)

@app.route("/status")
def view_status():
    contracts = get_all_contracts()
    return render_template("status.html", contracts=contracts)

@app.route("/download/<int:contract_id>")
def dowload_file(contract_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT file_path FROM contracts WHERE id = ?", (contract_id,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0]: 
        return send_file(result[0])
    else:
        return "PDF não encontrado!"

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        username = request.form.get("username")
        user_password = request.form.get("user_password")

    return render_template("registrar.html")

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)