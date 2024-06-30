import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

import pyodbc
from Factory.Empleado import Empleado

class EmpleadoService:
    def __init__(self) -> None:
        self.con = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};Server=localhost;Database=EXAMEN1;Port=1433;UID=sa;PWD=Gphv2021*;TrustServerCertificate=yes')

    def create(self,nom,ape,pue,cor,tel,dir):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_create \'{nom}\',\'{ape}\',\'{pue}\',\'{cor}\',{tel},\'{dir}\'")
            self.con.commit()
            return "Correcto"
        except Exception as e:
            return e
        
    def select(self):
        cursor = self.con.cursor()
        try:
            cursor.execute("EXEC SP_select")
            var = cursor.fetchall()
            array = [Empleado(row[0], row[1], row[2], row[3], row[4], row[5], row[6]).toJSON() for row in var]
            return array
        except Exception as e:
            return e
    
    def update(self,id,nom,ape,pue,cor,tel,dir):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_update {id},\'{nom}\',\'{ape}\',\'{pue}\',\'{cor}\',{tel},\'{dir}\'")
            self.con.commit()
            return "Correcto"
        except Exception as e:
            return e
    
    def delete(self,id):
        cursor = self.con.cursor()
        try:
            cursor.execute(f"exec SP_delete {id}")
            self.con.commit()
            return "Correcto"
        except Exception as e:
            return e
