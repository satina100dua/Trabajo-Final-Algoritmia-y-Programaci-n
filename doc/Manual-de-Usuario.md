# Manual de usuarios
Para ejecutar correctamente el programa, debe tener en cuenta que el sistema del parqueadero "La Guarderia" tiene el siguiente menú:
1. Registrar Usuario
2. Ingresar Vehículo
3. Retirar Vehículo
4. Administrador
5. Salir

El programa le solicitará ingresar una opción. En primer lugar es necesario que conozaca las funciones y restricciones de cada una de estas variables.
## 1. Registrar usuario
El usuario que ingrese al parqueadero será registrado con los siguientes datos y restricciones
- Nombre y Apellido: No puede tener menos de tres letras y no puede tener números.
- Documento: Debe ingresar entre 3 y 15 dígitos. Solo permite el ingreso de números.
- Placa: Debe tener exactamente 6 caracteres. Debe tener tres letras y luego tres números exactamente.

Todos los datos deben ser ingresados correctamente con las indicaciones planteadas, en caso contrario, se muestra un error.
## 2. Ingresar Vehículo
Solo los vehículos de usuarios registrados anteriormente serán aceptados por el sistema, para así, recepcionar su hora de entrada.
## 3. Retiro Vehículo
Solamente los vehículos de usuarios registrados podrán ser retirados del sistema. El cobro del servicio se determina de la siguiente manera:
- 7000 por hora
- 1500 por cada cuarto de hora

Teniendo así un total correspondiente a la suma del cobro por hora y el cobro por cuartos de hora.

El sistema también presentá una condición de pago mínimo, que se presenta si el total calculado es menor que el valor de una hora completa, en este caso se cumple que:
- El pago mínimo es de 7000
## 4. Administrador
En este módulo, el sistema solo permite acceso a quien tenga usuario y contraseña de administración. El submenú de administración contiene los siguientes reportes:
- Total de vehículos registrados
- Total de vehículos retirados
- Total de vehículos sin retirar
- Total pago de vehículos retirados
- Tiempo promedio de estancia por vehículo en el parqueadero
- Lista de usuarios
- Vehículo con tiempo de parqueo máximo y mínimo
## 5. Salir
Si ya no desea realizar más acciones, con esta opción podrá cerrar el sistema. O también puede implementar esta acción para ejecutar de nuevo otra función.

