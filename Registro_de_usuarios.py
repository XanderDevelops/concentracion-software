import pyodbc 

# Connection string for SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOPDANIEL\SQLSERVER;DATABASE=Registro de usuarios;UID=Grupo_1;PWD=123456789')
cursor = conn.cursor()

# Crear nuevo usuario
def create_User(user):
    cursor.execute("INSERT INTO Table_Estudiantes (ExternalID, UserEmail, UserPhone, Language, CreateUser, CreateDate, UpdateDate, UpdateUser, Password, Intent) VALUES (?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?, ?, ?)",
                   user['external_id'], user['email'], user['phone'], user['language'], user['create_user'], user['update_user'], user['password'], user['intent'])
    conn.commit()

# Leer todos los usuarios
def read_all_users():
    cursor.execute("SELECT * FROM Table_Estudiantes")
    return cursor.fetchall()

# Leer usuario por id
def read_user(id):
    cursor.execute("SELECT * FROM Table_Estudiantes WHERE ID = ?", id)
    return cursor.fetchone()

# Actualizar correo de los usuarios
def update_email(id, email):
    cursor.execute("UPDATE Table_Estudiantes SET UserEmail = ?, UpdateDate = GETDATE(), UpdateUser = 'python_script' WHERE ID = ?", email, id)
    conn.commit()

# Eliminar usuario
def delete_user(id):
    cursor.execute("DELETE FROM Table_Estudiantes WHERE ID = ?", id)
    conn.commit()

# Cerrar cursor y conexión
