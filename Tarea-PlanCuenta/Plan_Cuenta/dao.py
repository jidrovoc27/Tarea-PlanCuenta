import sys
sys.path.append('..\conexion')
from conexion import Conector

class Dao(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result= False
        try:
            sql="Select id, descripcion from grupo where descripcion like '%" + \
                str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresar(self, grup):
        correcto=True
        try:
            sql="insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql,grup.descripcion)
            self.conn.commit()
        except Exception as e:
            print("Error al insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificar(self, grup):
        correcto=True
        try:
            sql='Update grupo set descripcion = %s where id=%s'
            self.conectar()
            self.conector.execute(sql,(grup.descripcion, grup.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminar(self, grup):
        correcto=True
        try:
            sql='delete from grupo where id= %s'
            self.conectar()
            self.conector.execute(sql, (grup.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


    def consultarCuenta(self, buscar):
        result= False
        try:
            sql="Select Id, Codigo, grupo, Descripcion, Naturaleza, Estado from plancuenta where Descripcion like '%" + \
                str(buscar) + "%' order by Id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresarCuenta(self, cuent):
        correcto=True
        try:
            sql="insert into plancuenta (Codigo, grupo, Descripcion, Naturaleza, Estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,( cuent.codigo, cuent.grupo, cuent.descripcion, cuent.naturaleza, cuent.estado))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificarCuenta(self, cuent):
        correcto=True
        try:
            sql='Update plancuenta set Codigo = %s, grupo=%s, Descripcion=%s, Naturaleza=%s, Estado=%s where Id=%s'
            self.conectar()
            self.conector.execute(sql,( cuent.codigo, cuent.grupo, cuent.descripcion, cuent.naturaleza, cuent.estado, cuent.id))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminarCuenta(self, cuent):
        correcto=True
        try:
            sql='delete from plancuenta where Id= %s'
            self.conectar()
            self.conector.execute(sql, (cuent.id))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto