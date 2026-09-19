# ============================================================
# Sistema de Control de Acceso a un Parqueadero Universitario
# ============================================================

CUPOS_TOTALES = 30

# --- Entrada inicial ---
N = int(input("¿Cuántos vehículos se van a simular hoy?: "))
es_sabado_texto = input("¿Es sábado? (si/no): ").strip().lower()
es_sabado = es_sabado_texto == "si"

vehiculos_validos = 0
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

        vehiculos_validos = vehiculos_validos + 1
        print(f"Registro OK. Placa {placa} - Cobro: ${round(costo, 2)}")

        