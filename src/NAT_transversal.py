import sounddevice as sd
import minimal
import soundfile as sf
from NAT_minimal import Main

class Obtener_ip_puerto(Main):


    def __init__(self):
        super().__init__()

    def obtener_ip_puerto(self):
        destination_address = input("Ingrese la dirección IP de destino: ")
        listening_port = input("Ingrese el puerto de escucha: ")

        while True:
            destination_port = input("Ingrese el puerto de destino: ")
            
            try:
                destination_port = int(destination_port)
                break;
            except ValueError:
                    print("\033[91mEl puerto debe ser un número entero.\033[0m")
            
        return destination_address, listening_port, destination_port

# Obtén la dirección IP y el puerto del usuario
obtener_puerto = Obtener_ip_puerto()
destination_address, listening_port, destination_port = obtener_puerto.obtener_ip_puerto()

# Modifica directamente las opciones en minimal.parser
minimal.parser.set_defaults(destination_address=destination_address, listening_port=int(listening_port), destination_port=int(destination_port))

# Ejecuta el script minimal.py
minimal.args = minimal.parser.parse_args()
minimal.intercom = minimal.Minimal()
minimal.intercom.run()
