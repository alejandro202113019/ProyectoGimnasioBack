from utils.database import Database

db = Database()

def verificar_passwords():
    try:
        query = "SELECT `User`, `Password` FROM Login"
        usuarios = db.execute_query(query, dictionary=True)

        for usuario in usuarios:
            print(f"Usuario: {usuario['User']}, Contraseña: {usuario['Password']}")

    except Exception as e:
        print(f"Error verificando contraseñas: {e}")

if __name__ == "__main__":
    verificar_passwords()
