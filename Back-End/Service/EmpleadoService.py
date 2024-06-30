import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from Factory.Empleado import Empleado

class EmpleadoService:
    def __init__(self) -> None:
        self.empleados = []
        self.id = 0
    
    def create(self, nom, ape, pue, cor, tel, dir):
        self.id += 1;
        empleado = {
            'id': self.id,
            'nom': nom,
            'ape': ape,
            'pue': pue,
            'cor': cor,
            'tel': tel,
            'dir': dir
        }
        self.empleados.append(empleado)
        return "Correcto"
        
    def select(self):
        return [Empleado(e['id'], e['nom'], e['ape'], e['pue'], e['cor'], e['tel'], e['dir']).toJSON() for e in self.empleados]
    
    def update(self, id, nom, ape, pue, cor, tel, dir):
        for empleado in self.empleados:
            if empleado['id'] == id:
                empleado.update({
                    'nom': nom,
                    'ape': ape,
                    'pue': pue,
                    'cor': cor,
                    'tel': tel,
                    'dir': dir
                })
                return "Correcto"
        return f"Empleado con ID {id} no encontrado."
    
    def delete(self, id):
        for empleado in self.empleados:
            if empleado['id'] == id:
                self.empleados.remove(empleado)
                return "Correcto"
        return f"Empleado con ID {id} no encontrado."
