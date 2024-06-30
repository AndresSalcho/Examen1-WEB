class Empleado:
    def __init__(self,id,nom,ape,pue,cor,tel,dir) -> None:
        self.id_empleado = id
        self.nombres = nom
        self.apellidos = ape
        self.puesto = pue
        self.correo = cor
        self.telefono = tel
        self.direccion = dir
    
    def toJSON(self):
        return {
            'id_empleado': self.id_empleado,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'puesto': self.puesto,
            'correo': self.correo,
            'telefono': self.telefono,
            'direccion': self.direccion
        }