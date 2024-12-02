import bcrypt
from utils.database import Database

# Instancia de la clase Database
db = Database()

def actualizar_contrasenas():
    try:
        # Obtener usuarios con contraseñas en texto plano
        query_select = "SELECT `User`, `Password` FROM Login"
        usuarios = db.execute_query(query_select, dictionary=True)

        for usuario in usuarios:
            user = usuario['User']
            password_plano = usuario['Password']

            # Verificar si la contraseña ya está cifrada (bcrypt hashes comienzan típicamente con $2b$)
            if password_plano.startswith('$2b$'):
                print(f"La contraseña para el usuario {user} ya está cifrada. Se omite.")
                continue

            # Generar un hash bcrypt para la contraseña en texto plano
            password_hash = bcrypt.hashpw(password_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            # Actualizar la contraseña en la base de datos
            query_update = "UPDATE Login SET `Password` = %s WHERE `User` = %s"
            db.execute_query(query_update, (password_hash, user))
            print(f"Contraseña para el usuario {user} actualizada exitosamente.")

    except Exception as e:
        print(f"Error actualizando contraseñas: {e}")

if __name__ == "__main__":
    actualizar_contrasenas()
