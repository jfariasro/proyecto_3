import socket

def get_local_ip():
    """Obtiene la dirección IP local de la máquina"""
    try:
        # Conectarse a un servidor remoto para obtener la IP local
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    ip = get_local_ip()
    print("=" * 60)
    print("🌐 CONFIGURACIÓN PARA ACCESO EN RED LOCAL")
    print("=" * 60)
    print(f"📍 Tu IP local es: {ip}")
    print(f"🚀 Para acceder desde otros dispositivos, usa:")
    print(f"   http://{ip}:8000")
    print("")
    print("📋 PASOS PARA EJECUTAR EL SERVIDOR:")
    print("1. Ejecuta este comando en la terminal:")
    print(f"   python manage.py runserver {ip}:8000")
    print("")
    print("2. O también puedes usar:")
    print("   python manage.py runserver 0.0.0.0:8000")
    print("")
    print("📱 DISPOSITIVOS QUE PUEDEN CONECTARSE:")
    print("- Computadoras en la misma red WiFi")
    print("- Smartphones conectados al mismo WiFi")
    print("- Tablets y otros dispositivos móviles")
    print("")
    print("⚠️  IMPORTANTE:")
    print("- Asegúrate de que tu firewall permita conexiones en el puerto 8000")
    print("- Todos los dispositivos deben estar en la misma red WiFi")
    print("- Esta configuración es solo para desarrollo local")
    print("=" * 60)
