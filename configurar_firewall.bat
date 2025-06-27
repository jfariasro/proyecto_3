@echo off
echo ============================================================
echo 🔥 CONFIGURACION DEL FIREWALL PARA DJANGO
echo ============================================================
echo.
echo Este script configurara el firewall de Windows para permitir
echo acceso a Django desde otros dispositivos en la red WiFi.
echo.
echo 📋 Se ejecutaran los siguientes comandos:
echo.
echo 1. Agregar regla para puerto 8000 (entrada)
echo 2. Agregar regla para puerto 8000 (salida)  
echo 3. Mostrar estado actual del firewall
echo.
pause
echo.
echo 🔧 Configurando firewall...
echo.

REM Agregar regla de entrada para puerto 8000
netsh advfirewall firewall add rule name="Django Development Server (TCP-In)" dir=in action=allow protocol=TCP localport=8000

REM Agregar regla de salida para puerto 8000
netsh advfirewall firewall add rule name="Django Development Server (TCP-Out)" dir=out action=allow protocol=TCP localport=8000

echo.
echo ✅ Reglas del firewall agregadas exitosamente.
echo.
echo 📱 PARA CONECTARTE DESDE TU MOVIL:
echo.
echo 1. Asegurate de que tu movil este conectado a la misma red WiFi
echo 2. Ejecuta el servidor Django con:
echo    python manage.py runserver 0.0.0.0:8000
echo.
echo 3. En tu movil, abre el navegador y ve a:
echo    http://192.168.10.50:8000
echo.
echo 🔍 Para verificar la conexion:
echo - Desde tu PC: http://localhost:8000
echo - Desde otros dispositivos: http://192.168.10.50:8000
echo.
echo ⚠️  NOTA: Si aun no funciona, verifica que:
echo - Tu router no bloquee comunicacion entre dispositivos
echo - Tu antivirus no este bloqueando la conexion
echo - Ambos dispositivos esten en la misma red (no red de invitados)
echo.
pause
