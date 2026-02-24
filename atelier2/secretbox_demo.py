import argparse
from nacl.secret import SecretBox
from nacl.encoding import Base64Encoder
import os

def load_key():
    """Charge la clé secrète depuis le fichier secretbox.key."""
    try:
        with open("secretbox.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier secretbox.key est introuvable. Générez-le d'abord !")

def encrypt_file(input_file, output_file):
    """Chiffre un fichier avec SecretBox."""
    key = load_key()
    box = SecretBox(key)
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = box.encrypt(data, encoder=Base64Encoder)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    print(f"Fichier {input_file} chiffré avec succès dans {output_file}.")

def decrypt_file(input_file, output_file):
    """Déchiffre un fichier avec SecretBox."""
    key = load_key()
    box = SecretBox(key)
    with open(input_file, "rb") as f:
        encrypted = f.read()
    decrypted = box.decrypt(encrypted, encoder=Base64Encoder)
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"Fichier {input_file} déchiffré avec succès dans {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chiffrer/Déchiffrer un fichier avec SecretBox (PyNaCl).")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode : 'encrypt' ou 'decrypt'")
    parser.add_argument("input_file", help="Fichier d'entrée à chiffrer/déchiffrer")
    parser.add_argument("output_file", help="Fichier de sortie")
    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_file(args.input_file, args.output_file)
    else:
        decrypt_file(args.input_file, args.output_file)
