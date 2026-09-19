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

    print(f"Datos leídos -> Placa: {placa}, Tipo: {tipo_usuario}, Hora: {hora_entrada}, Horas: {horas_permanencia}")