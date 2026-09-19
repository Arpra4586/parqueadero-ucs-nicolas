
# Sistema de Control de Acceso a un Parqueadero Universitario


CUPOS_TOTALES = 30


N = int(input("¿Cuántos vehículos se van a simular hoy?: "))
es_sabado_texto = input("¿Es sábado? (si/no): ").strip().lower()
es_sabado = es_sabado_texto == "si"

vehiculos_validos = 0
i = 0


while i < N and vehiculos_validos < CUPOS_TOTALES:
    i = i + 1
    print(f"\n--- Vehículo #{i} ---")

   
    placa = input("Placa: ").strip().upper()
    tipo_usuario = input("Tipo de usuario (E=estudiante, D=docente, V=visitante): ").strip().upper()
    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecerá parqueado: "))

   
    hora_invalida = hora_entrada < 0 or hora_entrada > 23
    permanencia_invalida = horas_permanencia <= 0

    if hora_invalida or permanencia_invalida:
        print("ERROR: datos inválidos. Este vehículo no se contará en las estadísticas.")
    else:
    
        if not (tipo_usuario == "E" or tipo_usuario == "D" or tipo_usuario == "V"):
            tipo_usuario = "V"
            print("ADVERTENCIA: tipo de usuario no reconocido. Se tratará como visitante.")

        
        if tipo_usuario == "E":
            if horas_permanencia <= 2:
                costo = 0.0
            else:
                costo = (horas_permanencia - 2) * 800

        elif tipo_usuario == "D":
            costo = horas_permanencia * 500

        else:  # V - Visitante
            if horas_permanencia <= 1:
                costo = 1500
            else:
                costo = 1500 + (horas_permanencia - 1) * 1200

        vehiculos_validos = vehiculos_validos + 1
        print(f"Registro OK. Placa {placa} - Cobro: ${round(costo, 2)}")