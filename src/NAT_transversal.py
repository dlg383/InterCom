import argparse
import minimal

class NAT_transversal(minimal.Minimal):
    def obtener_ip_puerto(self):
        
        destination_address = input("Ingrese la dirección IP de destino: ")
        destination_port = input("Ingrese el puerto de destino: ")

        try:
            destination_port = int(destination_port)
        except ValueError:
            print("El puerto debe ser un número entero.")
            return None, None

        return destination_address, destination_port

    def run(self):
        # Obtiene la dirección IP y el puerto del usuario
        destination_address, destination_port = self.obtener_ip_puerto()

        if destination_address is not None and destination_port is not None:
            # Crea una instancia de la clase Minimal y ejecútala con los nuevos valores
            minimal.args.destination_address = destination_address
            minimal.args.destination_port = destination_port
            minimal.run()

if __name__ == "__main__":

    try:
        argcomplete.autocomplete(minimal.parser)
    except Exception:
        logging.warning("argcomplete not working :-/")

    minimal.args = minimal.parser.parse_known_args()[0]
    
    if minimal.args.list_devices:
        print("Available devices:")
        print(sd.query_devices())
        quit()

    if minimal.args.show_stats or minimal.args.show_samples:
        intercom = NAT_transversal()
        
    try:
        intercom.run()
    except KeyboardInterrupt:
        minimal.parser.exit("\nSIGINT received")
    finally:
        intercom.print_final_averages()

