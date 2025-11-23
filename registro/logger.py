def guardar_en_log(temp):
    with open("log.txt", "a") as f:
        f.write(f"{temp}\n")
