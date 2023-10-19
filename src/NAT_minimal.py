import stun

class Main:
    stun_servers = [
        'stun.l.google.com',
        'stun.ekiga.net',
        'stun.cheapvoip.com',
        'stun.gmx.de',
    ]

    def __init__(self):
        first_port = None  # Variable para almacenar el primer puerto
        puertos = set()  # Conjunto para almacenar los puertos
        no_simetrica = True
        ip = None
        puerto = None

        for stun_server in self.stun_servers:
            nat_type, external_ip, external_port = stun.get_ip_info(stun_host=stun_server)

            puertos.add(external_port)  # Agregar el puerto al conjunto

            if first_port is None:
                first_port = external_port
            elif external_port != first_port:
                no_simetrica = True
                ip = external_ip
                puerto = external_port

           # print("Server:" + stun_server)
            #print("NAT Type:" + str(nat_type))
            #print("External IP:" + str(external_ip))
            #print("External Port:" + str(external_port))

        if no_simetrica:
            print(f"La conexión no es simétrica. IP: {external_ip}, Puerto: {external_port}")
        else:
            print("La conexión es simétrica.")

a = Main()
