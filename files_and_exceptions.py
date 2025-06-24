def read_file_to_dict(filename):
    ventas_dict = {}
    with open(filename, 'r') as file:
        contenido = file.read().strip()
        ventas = contenido.split(';')
        for venta in ventas:
            if not venta:
                continue
            producto, valor = venta.split(':')
            valor = float(valor)
            if producto in ventas_dict:
                ventas_dict[producto].append(valor)
            else:
                ventas_dict[producto] = [valor]
    return ventas_dict



def process_dict(ventas_dict):
    for producto, montos in ventas_dict.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
