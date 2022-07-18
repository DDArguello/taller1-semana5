from usuarios import Rol


rol=Rol("David","0957436675","0982337416","darguello@gmail.com",1)
rol.mostrar()

rol=Rol(input("Ingrese nombre"),input("Ingrese cedula"),input("Ingrese telefono"),
    input("Ingrese correo"),int(input("Ingrese su id de rol")))
rol.mostrar()