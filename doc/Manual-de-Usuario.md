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
Para ingresar su vehículo, el usuario debe identificarse con su documento de identidad y la placa del automóvil. Una vez verificados los datos, el sistema registrará la hora de entrada y entregará un recibo con esta información.
## 3. Retiro Vehículo
Para realizar el retiro, el usuario debe identificar su vehículo ingresando la placa en el sistema. Solo podrán salir automóviles que estén registrados previamente. Al momento de la salida, el sistema generará una factura con los datos correspondientes y el valor total del servicio, calculado según el tiempo de uso:
- $7.000 por cada hora completa
- $1.500 por cada cuarto de hora adicional

Si el monto calculado es menor al valor de una hora, se cobrará un mínimo de $7.000.
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

