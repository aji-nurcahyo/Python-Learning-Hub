import struct

PACKET_FORMAT = struct.Struct("<Hff")  # uint16 node_id + float32 temp_c + float32 humidity_pct

node_id = 101
temp_c = 28.4
humidity = 62.0

binary_payload = PACKET_FORMAT.pack(node_id, temp_c, humidity)
ascii_equivalent = f"$TELEM,{node_id},{temp_c},{humidity}*00"

unpacked_id, unpacked_temp, unpacked_hum = PACKET_FORMAT.unpack(binary_payload)

print("Ukuran format biner :", PACKET_FORMAT.size, "bytes")
print("Ukuran format ASCII :", len(ascii_equivalent.encode('ascii')), "bytes")
print("Hex payload biner   :", binary_payload.hex(" "))
print("Hasil unpack        :", {"node_id": unpacked_id, "temp_c": round(unpacked_temp, 2), "humidity": round(unpacked_hum, 2)})

