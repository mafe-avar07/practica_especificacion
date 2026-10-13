'''
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh hasta 
150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh. Se 
necesita calcular el importe del recibo a partir del consumo del mes.
'''

#EJERCICIO 1: RECIBO DE LUZ
#PROBLEMA
#Calcular el importe del recibo mensual de electricidad a partir del consumo de energía registrado.

#ENTRADAS
#consumo_mensual: float, kWh, valor mayor o igual a 0.

#SALIDAS
#pago_mensual: float, pesos, importe del recibo con dos decimales.

#REGLAS Y SUPUESTOS
#1. La primera tarifa es de $1.00 por kWh hasta 150 kWh.
#2. La segunda tarifa es de $1.50 por kWh de 151 a 280 kWh.
#3. La tercera tarifa es de $3.00 por kWh mayor de 280 kWh.
#4. PENDIENTE: Confirmar si la tarifa seleccionada se aplica a todo el consumo o si cada tarifa  se aplica a únicamente a su bloque de kWh.
#5. El importe se mostrara con dos decimales.

#ALGORITMO
#1. Leer el consumo de energía mensual (kWh).
#2. Determinar la tarifa aplicable según el consumo:
#3. Calcular el importe según la interpretación confirmada en REGLAS Y SUPUESTOS.
#4. Mostrar el recibo con el importe calculado.

#CASOS DE PRUEBA



#RESRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#CONTRATO DE FUNCIONES
#leerConsumo() -> float:
#    Solicita y devuelve el consumo mensual en kWh como un número flotante mayor o igual a 0.

#calcularPago(consumo: float) -> float:
#    Calcula y devuelve el importe del recibo de luz según el consumo y las tarifas establecidas.

#mostrarRecibo(consumo: float, pago: float) -> None:
#    Muestra el recibo de luz con el consumo y el importe calculado, formateado con dos decimales.

def leerConsumo():
    consumo_mensual = float(input("Ingrese el consumo mensual en kWh (mayor o igual a 0): "))
    return consumo_mensual

def calcularPago(consumo: float):
    if consumo <= 150:
        pago_mensual = consumo * 1.00
    elif consumo == 150 and consumo <= 280:
        pago_mensual = (150 * 1.00) + ((consumo - 150) * 1.50)
    else:
        pago_mensual = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
    
    return round(pago_mensual, 2)