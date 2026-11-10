import serial

# Menggunakan pySerial virtual loopback URL ('loop://') untuk simulasi port serial offline
ser = serial.serial_for_url("loop://", baudrate=115200, timeout=0.5)
try:
    frames = [
        b"$TELEM,101,28.4,62.0,3.85*7F\n",
        b"$TELEM,102,29.1,60.5,3.82*78\n",
    ]
    for frame in frames:
        ser.write(frame)

    received = []
    for _ in range(len(frames)):
        line = ser.readline().decode("ascii", errors="replace").strip()
        received.append(line)

    print("Port simulasi terbuka :", ser.is_open, "| port:", ser.port)
    print("Frame terbaca loopback:", received)
finally:
    ser.close()

