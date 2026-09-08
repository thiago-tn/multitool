import secrets


def password_generator(length=None):
    if length is None:
        length = int(input("Digite o comprimento da senha: "))

    if length < 1:
        raise ValueError("O comprimento deve ser maior que zero.")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    return "".join(secrets.choice(characters) for _ in range(length))