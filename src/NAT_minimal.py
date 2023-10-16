import stun

class Main:
    stun_servers = [
        'stun.l.google.com',
        'stun.ekiga.net',
        'stun.cheapvoip.com',
        'stun.gmx.de',
        'stun.gmx.net',
    ]

    def __init__(self):
        first_port = None  # Variable para almacenar el primer puerto
        hay_puertos_diferentes = False  # Variable para indicar si hay puertos diferentes

        for stun_server in self.stun_servers:
            nat_type, external_ip, external_port = stun.get_ip_info(stun_host=stun_server)

            print("Server:" + stun_server)
            print("NAT Type:" + str(nat_type))
            print("External IP:" + str(external_ip))
            print("External Port:" + str(external_port))

            # Si es la primera iteración, asigna el puerto a la variable first_port
            if first_port is None:
                first_port = external_port
            else:
                # Comparar el puerto actual con el primer puerto
                if external_port == first_port:
                    print(f"El puerto es igual a {first_port}!\n")
                else:
                    print(f"El puerto NO es igual a {first_port}.\n")
                    hay_puertos_diferentes = True

        if hay_puertos_diferentes:
            print("La conexión es simétrica.")
        else:
            print("La conexión no es simétrica.")

a = Main()
