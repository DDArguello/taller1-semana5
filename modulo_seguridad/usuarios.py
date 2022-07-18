class Usuario:
    def __init__(self,nombre,cedula,correo,telef):
        self.name=nombre
        self.ced=cedula
        self.correo=correo
        self.telefono=telef
    

# class UserAdmin(Usuario):
    
#     def __init__(self,nombre,ced,telf,correo,id_user=1):
#        # if id_rol==1:
#            # self.id_rol="Administrador"
#         if id_user==1:
#             self.id_user="Seguridad del sistema"

#         super().__init__(ced,nombre,telf,correo)
    
    

# class UserOper(Usuario):
    
#     def __init__(self,nombre,ced,telf,correo,id_user=2):
#         #if id_rol==2:
#             #self.id_rol="Operador"
#         if id_user==2:
#             self.id_user="Mantenimiento del sistema"
    
#         super().__init__(ced,nombre,telf,correo)
        
#     def mostrar(self):
#         print(f"Usuario: {self.ced} {self.name} {self.correo} {self.telefono} Cargo: {self.id_rol} de {self.id_user}")


class Rol(Usuario):
    def __init__(self,nombre,ced,telf,correo,id_rol,id_user=0):
        if id_rol==2:
            self.id_rol="Operador"
            id_user=1
            if id_user==1:
                self.id_user="Seguridad del sistema"
        elif id_rol==1:
            self.id_rol="Administrador"
            id_user=2
            if id_user==2:
                self.id_user="Mantenimiento del sistema"
        else:
            self.id_rol="none"
    
        super().__init__(ced,nombre,telf,correo)
        
    def mostrar(self):
        print(f"Usuario: {self.ced} {self.name} {self.correo} {self.telefono} Rol: {self.id_rol} - con accesso a: {self.id_user}")

if __name__ == "__main__":

    rol=Rol("David","0957436675","0982337416","darguello@gmail.com",1)
    rol.mostrar()