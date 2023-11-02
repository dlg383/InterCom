import stun

class Main:
    stun_servers = [
        "stun.1und1.de",
    "stun.gmx.net",
    "stun.l.google.com",
    "stun1.l.google.com",
    ]

    def __init__(self):
        first_port = None  # Variable para almacenar el primer puerto
        puertos = set()  # Conjunto para almacenar los puertos
        cont = 0

        for stun_server in self.stun_servers:
            nat_type, external_ip, external_port = stun.get_ip_info(stun_host=stun_server)
            
            if external_port and external_ip is None or external_port is None or external_ip is None:  # Verificar si external_port es None
                continue

            puertos.add(external_port)  # Agregar el puerto al conjunto
            
            
            print("###########################################")
            print("Recorrido")
            print(cont) 
            print("Server:" + stun_server)
            print("NAT Type:" + str(nat_type))
            print("External IP:" + str(external_ip))
            print("External Port:" + str(external_port))
            cont = cont + 1

            if first_port is None:
                first_port = external_port
            elif external_port != first_port:
                print("LA CONEXIÓN NO FUNCIONA")
                return

        if len(puertos) == 1:
            print("###########################################")
            print("###########################################")
            print("###########################################")

            print(f"La conexión es  NO SIMETRICA. Puerto: {first_port} IP: {external_ip}")
        else:
            print("LA CONEXIÓN NO FUNCIONA")

a = Main()
