from uuid import getnode


def obtener_direccion_mac():
    print(getnode())
    mac = hex(getnode())
    mac = mac.zfill(12)
    mac = mac.replace('0x', '').upper()
    print(mac[i: i+2] for i in range(0, 11, 2))

    direccion_mac = ":".join(mac[i: i+2] for i in range(0, 11, 2))
    return direccion_mac


direccion_mac = obtener_direccion_mac()
print(direccion_mac)
