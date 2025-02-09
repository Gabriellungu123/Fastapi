from modelo.plato import Plato

class DaoPlatos:
    
    def get_all(self,db) -> list[Plato]:
        cursor = db.cursor()
    
        cursor.execute("SELECT * FROM platos")

        equipos_en_db = cursor.fetchall()
        equipos : list[Plato]= list()
        for equipo in equipos_en_db:
            plato = Plato(equipo[0], equipo[1])
            equipos.append(plato)
        cursor.close()
        
        return equipos
    
    def insert(self, db, nombre: str):
        cursor = db.cursor()
        sql = ("INSERT INTO platos (nombre) values (%s) ")
        data = (nombre,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO platos (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def delete(self, db, id: str):
        cursor = db.cursor()
        sql = ("DELETE FROM  plato where id = (%s) ")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO plato (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()