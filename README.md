CONTROL DE ASISTENCIAS Y VACACIONES EN UN HOSPITAL 

  1.- Datos del trabajador:

  Nombre completo  
  
  Número del empleado (ID)
  
  Genero 
  
  Edad
  
  2.-puesto 

  Médico 

 Enfermera 

 Limpieza

 Seguridad 
 

  3.-Registro de asitencia diaria:
  
  Asistió(Presente)
  
  Falto(Ausente)
  
  Retraso(Opcional)
  
  Esta de vacaciones 
  
  Dia libre 
  

  3.-Turnos:
  
  -En un hospital hay diferentes horarios 
  
  Matutino (mañana)
     
  Vespertino (tarde)
     
  Nocturno (noche)


 4.-Vacaciones:

-Cada trabajador tiene derecho a ciertos días de vacaciones por año ( por ejemplo: 15 días )

ene - feb
 
feb - mar 

mar - abr 

abr - may 

may - jun 

jun - jul

jul - ag 

ago - sep

sep - oct

oct - nov
 
nov - dic  

Saber que días ya lo ha usado

Marcar esos dias como "VACACIONES" en el registro


   5.-Control de fechas importantes tener en cuenta : 
   
  El calendario laboral( fines de semana, feriado) 
       
  Evitar que se registren vacaciones en días no laborales si no corresponden 
       
  Validar que las fechas ingresadas tengan sentido (inicio antes del fin)




  VACACIONES(BOTONES-CLASS):

Este es un código que selecciona un empleado desde un menú, asigna un periodo de vacaciones y muestra la confirmación y este evita que otro trabajador elija su mismo periodo de vacaciones

Este código sirve para administrar y seleccionar vacaciones a empleados de una forma sencilla para administrar de forma de una interfaz visual.

Esto es algo de información de la estructura del codigo :

Messagebox:

Messagebox es un submódulo de tkinter que permite mostrar ventanas emergentes (como alertas o mensajes de confirmación).

Class Empleado:

Se define una clase llamada Empleado, las clases son moldes para crear objetos, representamos a cada empleado como un objeto con nombre y sus vacaciones.

Root: la ventana principal de Tkinter.

Método para Generar Periodos:

Def generar_periodos(self):

método que construye los periodos vacacionales.

Meses : Ene, Feb, Mar, Abr, May, Jun, Jul, Ag, Sep, Oct, Nov, Dic

Return f”{mes} 01 – {mes} 15” for mes in meses + f”{mes} 16 – {mes} 30” for mes in meses

Generar:

Periodos del 1 al 15 para cada mes.

Periodos del 16 al 30 para cada mes.





       
