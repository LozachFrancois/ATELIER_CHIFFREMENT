import os
from cryptography.fernet import Fernet

def load_key() -> bytes:
    """
    Charge la clé depuis la variable d'environnement FERNET_KEY.
    Si absente, on en génère une et on l'affiche pour que l'étudiant la copie.
    """
    key = os.environ.get("FERNET_KEY")
    if not key:
        new_key = Fernet.generate_key()
        print("⚠️  Aucune clé trouvée (FERNET_KEY). Voici une clé générée :")
        print(new_key.decode())
        print("\n➡️  Copie-la ensuite dans l'environnement, ex :")
        print("export FERNET_KEY='" + new_key.decode() + "'")
        return new_key
    return key.encode()

def main():
    key = load_key()
    f = Fernet(key)

    message = "Bonjour, ceci est un secret !"
    token = f.encrypt(message.encode("utf-8"))

    print("\n=== Chiffrement ===")
    print("Message clair :", message)
    print("Token chiffré :", token.decode("utf-8"))

    print("\n=== Déchiffrement ===")
    clear = f.decrypt(token).decode("utf-8")
    print("Message déchiffré :", clear)

if __name__ == "__main__":
    main()

