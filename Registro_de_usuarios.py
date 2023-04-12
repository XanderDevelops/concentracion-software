# import pyodbc

# # Connection string for SQL Server
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOPDANIEL\SQLSERVER;DATABASE=Registro de usuarios;UID=Grupo_1;PWD=123456789')
# cursor = conn.cursor()

# #print(conn)

# def check_id(id, email, phone, username, language, create_user, create_date, UpdateDate, UpdateUser, password, intent, estado):
#     if(read_user(id) == None):
#         create_User(id, email, phone, username, language, create_user, create_date, UpdateDate, UpdateUser, password, intent, estado)
#     else:
#         print("id existe")

# # Crear nuevo usuario
# def create_User(id, email, phone, username, language, create_user, create_date, UpdateDate, UpdateUser, password, intent, estado):

#     cursor.execute("INSERT INTO Table_Estudiantes (ID, UserEmail, Username, UserPhone, Language, CreateUser, CreateDate, UpdateDate, UpdateUser, Password, Intent, Estado) VALUES (?, ?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?, ?, ?)",
#                    id, email, username, phone, language, create_user, create_date, password, intent, estado)
#     conn.commit()
    

# # Leer todos los usuARIOS
# def read_all_users():
#     cursor.execute("SELECT * FROM Table_Estudiantes")
#     return cursor.fetchall()

# # Leer usuario por id
# def read_user(id):
#     cursor.execute("SELECT * FROM Table_Estudiantes WHERE ID = ?", id)
#     return cursor.fetchone()

# # Actualizar correo de los usuarios
# def update_email(id, email):
#     cursor.execute(f"UPDATE Table_Estudiantes SET UserEmail = ?, UpdateDate = GETDATE(), UpdateUser = 'python_script' WHERE ID = ?", email, id)
#     conn.commit()

# # Eliminar usuario
# def delete_user(id):
#     cursor.execute(f"DELETE FROM Table_Estudiantes WHERE ID = ?", 1)
#     conn.commit()

# # Ejemplo
# #user_id = 'b1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
# #check_id(user_id, username, 'test@example.com', '555-555-1212', 'en-US', 'python_script', 'password123', 1, 0)
# #print(read_user(user_id))
# #update_email(user_id, 'new_email1@example.com')
# #print(read_user(user_id))
# #delete_user(user_id)
# #print(read_all_users())

# # Cerrar cursor y conexión
# cursor.close()
# conn.close()


import pyodbc 

# Connection string for SQL Server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOPDANIEL\SQLSERVER;DATABASE=Registro de usuarios;UID=Grupo_1;PWD=123456789')
cursor = conn.cursor()

# Crear nuevo usuario
def create_User(user):
    cursor.execute("INSERT INTO Table_Estudiantes (id, UserEmail, Username, UserPhone, Language, CreateUser, CreateDate, UpdateDate, UpdateUser, Password, Intent, Estado) VALUES (NEWID(), ?, ?, ?, ?, ?, GETDATE(), GETDATE(), ?, ?, ?, ?)",
                   user['email'], user['username'], user['phone'], user['language'], user['create_user'], user['update_user'], user['password'], user['intent'], user['estado'])
    conn.commit()

# Leer todos los usuarios
def read_all_users():
    cursor.execute("SELECT * FROM Table_Estudiantes")
    return cursor.fetchall()

# Leer usuario por id
def read_user(id):
    cursor.execute("SELECT * FROM Table_Estudiantes WHERE ID = ?", id)
    return cursor.fetchone()
# Get username 
def get_username(username):
    cursor.execute("SELECT * FROM Table_Estudiantes WHERE USERNAME = ?", username)
    return cursor.fetchone()

# Get Password
def get_password(password):
    cursor.execute("SELECT * FROM Table_Estudiantes WHERE PASSWORD = ?", password)
    return cursor.fetchone()

# Actualizar correo de los usuarios
def update_email(id, email):
    cursor.execute("UPDATE Table_Estudiantes SET UserEmail = ?, UpdateDate = GETDATE(), UpdateUser = 'python_script' WHERE ID = ?", email, id)
    conn.commit()

# Eliminar usuario
def delete_user(id):
    cursor.execute("DELETE FROM Table_Estudiantes WHERE ID = ?", id)
    conn.commit()

def get_password(username):
    cursor.execute("SELECT Password FROM Table_Estudiantes WHERE USERNAME = ?", username)
    return cursor.fetchone()
def get_status(username):
    cursor.execute("SELECT username FROM Table_Estudiant WHERE USERNAME = ?", username)
# Cerrar cursor y conexión
