def tampilkan_sinyal(rsrp, satuan="dBm"):
    return f"{rsrp} {satuan}"

print(tampilkan_sinyal(-91))
print(tampilkan_sinyal(-88, satuan="dBm"))
