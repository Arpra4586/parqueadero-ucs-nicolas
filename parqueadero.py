# ============================================================
# Sistema de Control de Acceso a un Parqueadero Universitario
# ============================================================

CUPOS_TOTALES = 30

# --- Entrada inicial ---
N = int(input("¿Cuántos vehículos se van a simular hoy?: "))
es_sabado_texto = input("¿Es sábado? (si/no): ").strip().lower()
es_sabado = es_sabado_texto == "si"

# --- Acumuladores / contadores (sin listas ni diccionarios) ---
vehiculos_validos = 0
total_recaudado = 0.0
cant_estudiantes = 0
cant_docentes = 0
cant_visitantes = 0
suma_horas_permanencia = 0.0
i = 0

# --- Ciclo principal: while con corte por cupos ---
while i < N and vehiculos_validos < CUPOS_TOTALES:
    i = i + 1
    print(f"\n--- Vehículo #{i} ---")

    # Entrada de datos (estructura secuencial + tipos de datos)
    placa = input("Placa: ").strip().upper()
    tipo_usuario = input("Tipo de usuario (E=estudiante, D=docente, V=visitante): ").strip().upper()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecerá parqueado: "))

    # Validaciones con estructuras de decision + operador logico
    hora_invalida = hora_entrada < 0 or hora_entrada > 23
    permanencia_invalida = horas_permanencia <= 0

    if hora_invalida or permanencia_invalida:
        print("ERROR: datos inválidos. Este vehículo no se contará en las estadísticas.")
    else:
        # Tipo de usuario por defecto si no es E, D o V
        if not (tipo_usuario == "E" or tipo_usuario == "D" or tipo_usuario == "V"):
            tipo_usuario = "V"
            print("ADVERTENCIA: tipo de usuario no reconocido. Se tratará como visitante.")

        # Calculo de tarifa (if-elif-else anidado)
        if tipo_usuario == "E":
            if horas_permanencia <= 2:
                costo = 0.0
            else:
                costo = (horas_permanencia - 2) * 800

        elif tipo_usuario == "D":
            costo = horas_permanencia * 500

        else:  # V - Visitante
            tarifa_primera_hora = 1500
            tarifa_hora_adicional = 1200

            # Bonus: sábado reduce tarifas de visitante un 20%
            if es_sabado:
                tarifa_primera_hora = tarifa_primera_hora * 0.8
                tarifa_hora_adicional = tarifa_hora_adicional * 0.8

            if horas_permanencia <= 1:
                costo = tarifa_primera_hora
            else:
                costo = tarifa_primera_hora + (horas_permanencia - 1) * tarifa_hora_adicional

        # Descuento nocturno: NO aplica si es sábado (regla del bonus)
        if not es_sabado and (hora_entrada >= 19 or hora_entrada < 6):
            costo = costo * 0.9

        costo = round(costo, 2)

        # Acumular estadisticas
        vehiculos_validos = vehiculos_validos + 1
        total_recaudado = total_recaudado + costo
        suma_horas_permanencia = suma_horas_permanencia + horas_permanencia

        if tipo_usuario == "E":
            cant_estudiantes = cant_estudiantes + 1
        elif tipo_usuario == "D":
            cant_docentes = cant_docentes + 1
        else:
            cant_visitantes = cant_visitantes + 1

        print(f"Registro OK. Placa {placa} - Cobro: ${costo}")

        # Control de cupos
        if vehiculos_validos == CUPOS_TOTALES:
            print("\nPARQUEADERO LLENO")

# --- Salida formateada ---
if vehiculos_validos > 0:
    promedio_horas = round(suma_horas_permanencia / vehiculos_validos, 1)
else:
    promedio_horas = 0.0

porcentaje_ocupacion = round((vehiculos_validos / CUPOS_TOTALES) * 100, 1)

print("\n====== RESUMEN DEL DIA ======")
print(f"Vehiculos registrados: {vehiculos_validos}/{CUPOS_TOTALES}")
print(f"Ocupacion: {porcentaje_ocupacion}%")
print(f"Recaudo total: ${round(total_recaudado, 2)}")
print(f"Estudiantes: {cant_estudiantes} | Docentes: {cant_docentes} | Visitantes: {cant_visitantes}")
print(f"Promedio de permanencia: {promedio_horas} horas")
print("==============================")