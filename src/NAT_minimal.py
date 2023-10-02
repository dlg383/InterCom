import stun

class Main:
    stun_servers = [
        'stun.l.google.com',
        'stun.ekiga.net',
        'stun.cheapvoip.com',
        'stun.gmx.de',
        'stun.gmx.net',
        'stun.ipfire.org',
        'stun.linphone.org',
        'stun.services.mozilla.com',
        'stun.stunprotocol.org',
        'stunserver.org'
    ]

        nat_types = [0]
        external_ips = [0]
        external_ports = [0]

    #def print_info(self):
        for i in range(len(stun_servers)):
            print(f"Server: {stun_servers[i]}")
            print(f"NAT Type: {nat_types[i]}")
            print(f"External IP: {external_ips[i]}")
            print(f"External Port: {external_ports[i]}\n")

    def print_stun_servers(self):
        print("Lista de servidores STUN:")
        for server in self.stun_servers:
            print(server)