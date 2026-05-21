import sys
sys.path.append('..')
from conexion import conectar

def crear_pedido_cabecera(id_usuario, id_mesa, id_estado, id_tipo):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            # RETURNING nos devuelve el ID generado por el SERIAL de Postgres al instante
            sql = """INSERT INTO PedidoVenta (Usuario_idUsuario, Mesa_idMesa, EstadoPedido_idEstado, TipoPedido_idTipoPedido) 
                     VALUES (%s, %s, %s, %s) RETURNING idPedidoVenta;"""
            cursor.execute(sql, (id_usuario, id_mesa, id_estado, id_tipo))
            id_pedido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            return id_pedido
        except Exception as e:
            print(f"Error al aperturar comanda: {e}")
            return None

def agregar_item_a_pedido(id_pedido, id_producto, cantidad, precio_unitario):
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            subtotal = cantidad * precio_unitario
            sql = """INSERT INTO DetallePedidoVenta (cantidad, precioUnitario, subtotal, PedidoVenta_idPedidoVenta, Productos_idProductos) 
                     VALUES (%s, %s, %s, %s, %s);"""
            cursor.execute(sql, (cantidad, precio_unitario, subtotal, id_pedido, id_producto))
            
            # Actualizamos de forma automática el total acumulado en la cabecera de la venta
            sql_update_total = "UPDATE PedidoVenta SET totalPedido = totalPedido + %s WHERE idPedidoVenta = %s;"
            cursor.execute(sql_update_total, (subtotal, id_pedido))
            
            conn.commit()
            print(f"Item agregado al pedido N° {id_pedido}.")
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"Error al agregar producto al detalle: {e}")