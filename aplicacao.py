from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'gsbrielroot',
    'password': '12345678',
    'database': 'aula_13_10',
    'raise_on_warnings': True
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# Rota principal
@app.route('/')
def index():
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    return render_template('index.html', funcionarios=funcionarios)

# Rota para o formulário
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        setor = request.form['setor']
        cargo = request.form['cargo']
        id_setor = request.form['idSetor']
        id_cargo = request.form['idCargo']
        primeiro_nome = request.form['firstName']
        sobrenome = request.form['lastName']
        data_admissao = request.form['admissionDate']
        status = request.form['status']

        # Insira os dados no banco de dados
        cursor.execute('INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, cargo, id_cargo) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (primeiro_nome, sobrenome, data_admissao, status == 'ativo', id_setor, cargo, id_cargo))
        conn.commit()

        return redirect(url_for('index'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
