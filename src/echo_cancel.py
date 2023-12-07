import numpy as np
import buffer  # Asegúrate de que buffer está correctamente definido
import argparse
import sounddevice as sd
import socket
import time
import psutil
import math
import struct
import threading
import minimal
import soundfile as sf
import logging

class EchoCancel(buffer.Buffering):
    def __init__(self):
        super().__init__()

    def calculate_echo_delay_and_attenuation(self):
        self.echo_delay = 100000 
        self.echo_attenuation = 0.5

    def cancel_echo(self, chunk):
        delayed_chunk = np.roll(chunk, self.echo_delay)
        delayed_chunk[:self.echo_delay] = 0
        return chunk - self.echo_attenuation * delayed_chunk

    def _record_io_and_play(self, indata, outdata, frames, time, status):
        self.chunk_number = (self.chunk_number + 1) % self.CHUNK_NUMBERS
        indata = self.cancel_echo(indata)
        packed_chunk = self.pack(self.chunk_number, indata)
        self.send(packed_chunk)
        chunk = self.unbuffer_next_chunk()
        self.play_chunk(outdata, chunk)

    def _read_io_and_play(self, outdata, frames, time, status):
        self.chunk_number = (self.chunk_number + 1) % self.CHUNK_NUMBERS
        read_chunk = self.read_chunk_from_file()
        read_chunk = self.cancel_echo(read_chunk)
        packed_chunk = self.pack(self.chunk_number, read_chunk)
        self.send(packed_chunk)
        chunk = self.unbuffer_next_chunk()
        self.play_chunk(outdata, chunk)

# Crea una instancia de la clase EchoCancel
echo_cancel_instance = EchoCancel()

# Asigna la instancia a buffer.intercom
buffer.intercom = echo_cancel_instance

# Ejecuta el método run de la instancia
echo_cancel_instance.run()
