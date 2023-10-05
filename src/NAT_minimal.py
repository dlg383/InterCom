import stun

class Main:
    stun_servers = [
        'stun.l.google.com',
        'stun.ekiga.net',
        'stun.cheapvoip.com',
        'stun.gmx.de',
        'stun.gmx.net',
        ]

    nat_type = [] * 5
    external_ip = [] * 5
    external_port = [] * 5

    for stun_servers in stun_servers:
        nat_type, external_ip, external_port = stun.get_ip_info(stun_host= stun_servers)

        print("Server:" + stun_servers)
        print("NAT Type:" + str(nat_type))
        print("External IP:" + str(external_ip))
        print("External Port:" + str(external_port) + "\n")
            

a = Main()
