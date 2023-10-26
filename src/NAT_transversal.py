import os
import stun
from NAT_minimal import Main
from minimal import Minimal

class ClaseHereda(Main):
    def __init__(self):
        super().__init__()

minimal_script_path = os.path.join(os.path.dirname(__file__), 'minimal.py')
os.system(f'python {minimal_script_path}')