from conexion import conectar

conexion = conectar()

if conexion:
    try:
        cursor = conexion.cursor()
        
        tablas = [
            # --- TABLAS MAESTRAS (Nivel 0 - No tienen dependencias) ---
            '''CREATE TABLE IF NOT EXISTS TipoMovimiento(
                idTipoMovimiento SERIAL PRIMARY KEY,
                nombreTpMov VARCHAR(50) NOT NULL,
                descripcionTpMov VARCHAR(100) NOT NULL
            );''',
            '''CREATE TABLE IF NOT EXISTS TipoDocumento(
                idTipoDocumento SERIAL PRIMARY KEY,
                nombreTpDoc VARCHAR(50) NOT NULL,
                descripcionTpDoc VARCHAR(100) NOT NULL
            );''',
            '''CREATE TABLE IF NOT EXISTS Roles(
                idRoles SERIAL PRIMARY KEY,
                nombreRol VARCHAR(45) NOT NULL,
                descripcionRol VARCHAR(100) NOT NULL
            );''',
            '''CREATE TABLE IF NOT EXISTS EstadoMesa(
                idEstadoMesa SERIAL PRIMARY KEY,
                nombreEstadoMs VARCHAR(45) NOT NULL,
                activoEstadoMs BOOLEAN DEFAULT TRUE
            );''',
            '''CREATE TABLE IF NOT EXISTS EstadoPedido(
                idEstado SERIAL PRIMARY KEY,
                nombreEstadoPd VARCHAR(45) NOT NULL,
                descripcionEstadoPd VARCHAR(100),
                activoEstadoPd BOOLEAN DEFAULT TRUE
            );''',
            '''CREATE TABLE IF NOT EXISTS TipoPedido(
                idTipoPedido SERIAL PRIMARY KEY,
                nombreTpPedido VARCHAR(45) NOT NULL
            );''',
            '''CREATE TABLE IF NOT EXISTS MetodoPago(
                idMetodoPago SERIAL PRIMARY KEY,
                nombreMetodo VARCHAR(45) NOT NULL,
                activoMetodo BOOLEAN DEFAULT TRUE
            );''',
            '''CREATE TABLE IF NOT EXISTS EstadoRecibo(
                idEstadoRecibo SERIAL PRIMARY KEY,
                nombreEstadoRcb VARCHAR(45) NOT NULL,
                descripcionEstadoRcb VARCHAR(100),
                activoEstadoRcb BOOLEAN DEFAULT TRUE
            );''',
            '''CREATE TABLE IF NOT EXISTS EstadoCaja(
                idEstadoCaja SERIAL PRIMARY KEY,
                nombreEstadoCj VARCHAR(45) NOT NULL
            );''',
            '''CREATE TABLE IF NOT EXISTS CategoriaProducto(
                idcategoria SERIAL PRIMARY KEY,
                nombreCategoria VARCHAR(45) NOT NULL,
                descripcionCategoria VARCHAR(100)
            );''',
            '''CREATE TABLE IF NOT EXISTS Caja(
                idCaja SERIAL PRIMARY KEY,
                nombreCaja VARCHAR(45) NOT NULL,
                descripcionCaja VARCHAR(100),
                activoCaja BOOLEAN DEFAULT TRUE
            );''',
            
            # --- TABLAS RELACIONADAS NIVEL 1 ---
            '''CREATE TABLE IF NOT EXISTS Usuario(
                idUsuario SERIAL PRIMARY KEY,
                nombresUsuario VARCHAR(50) NOT NULL,
                apellidosUsuario VARCHAR(50) NOT NULL,
                documentoUsuario BIGINT NOT NULL,
                correoUsuario VARCHAR(50) NOT NULL,
                passwordUsuario VARCHAR(255),
                telefonoUsuario BIGINT NOT NULL,
                direccionUsuario VARCHAR(50) NOT NULL,
                TipoDocumento_idTipoDocumento INT NOT NULL,
                Roles_idRoles INT NOT NULL,
                CONSTRAINT fk_usuario_tipoDocumento FOREIGN KEY (TipoDocumento_idTipoDocumento) REFERENCES TipoDocumento(idTipoDocumento),
                CONSTRAINT fk_usuario_roles FOREIGN KEY (Roles_idRoles) REFERENCES Roles(idRoles)
            );''',
            '''CREATE TABLE IF NOT EXISTS Mesa(
                idMesa SERIAL PRIMARY KEY,
                numeroMesa INT NOT NULL,
                EstadoMesa_idEstadoMesa INT NOT NULL,
                CONSTRAINT fk_mesa_estadoMesa FOREIGN KEY (EstadoMesa_idEstadoMesa) REFERENCES EstadoMesa(idEstadoMesa)
            );''',
            '''CREATE TABLE IF NOT EXISTS Productos(
                idProductos SERIAL PRIMARY KEY,
                nombrePlato VARCHAR(45) NOT NULL,
                descripcion VARCHAR(100),
                precioVenta NUMERIC(10, 2) NOT NULL,
                activoProd BOOLEAN DEFAULT TRUE,
                CategoriaProducto_idcategoria INT NOT NULL,
                CONSTRAINT fk_productos_categoria FOREIGN KEY (CategoriaProducto_idcategoria) REFERENCES CategoriaProducto(idcategoria)
            );''',
            
            # --- TABLAS RELACIONADAS NIVEL 2 (Flujo de Caja y Pedidos) ---
            '''CREATE TABLE IF NOT EXISTS AperturaCierreCaja(
                idAperturaCierreCaja SERIAL PRIMARY KEY,
                fechaApertura TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                montoInicial NUMERIC(10,2) NOT NULL,
                fechaCierre TIMESTAMP,
                montoFinalSistema NUMERIC(10,2),
                montoFinalReal NUMERIC(10,2),
                diferencia NUMERIC(10,2),
                Caja_idCaja INT NOT NULL,
                UsuarioOpen_idusuario INT NOT NULL,
                UsuarioClos_idusuario INT,
                EstadoCaja_idEstadoCaja INT NOT NULL,
                CONSTRAINT fk_apertura_caja FOREIGN KEY (Caja_idCaja) REFERENCES Caja(idCaja),
                CONSTRAINT fk_apertura_usuario_open FOREIGN KEY (UsuarioOpen_idusuario) REFERENCES Usuario(idUsuario),
                CONSTRAINT fk_apertura_usuario_close FOREIGN KEY (UsuarioClos_idusuario) REFERENCES Usuario(idUsuario),
                CONSTRAINT fk_apertura_estado FOREIGN KEY (EstadoCaja_idEstadoCaja) REFERENCES EstadoCaja(idEstadoCaja)
            );''',
            '''CREATE TABLE IF NOT EXISTS MovimientoCaja(
                idMovimientoCaja SERIAL PRIMARY KEY,
                valorMvCaja NUMERIC(10,2) NOT NULL,
                descripcionMvCaja VARCHAR(200) NOT NULL,
                fechaMvCaja TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                TipoMovimiento_idTipoMovimiento INT NOT NULL,
                AperturaCierreCaja_idAperturaCierreCaja INT NOT NULL,
                Usuario_idUsuario INT NOT NULL,
                CONSTRAINT fk_movimientoCaja_TipoMovimiento FOREIGN KEY (TipoMovimiento_idTipoMovimiento) REFERENCES TipoMovimiento(idTipoMovimiento),
                CONSTRAINT fk_MovimientoCaja_AperturaCierreCaja FOREIGN KEY (AperturaCierreCaja_idAperturaCierreCaja) REFERENCES AperturaCierreCaja(idAperturaCierreCaja),
                CONSTRAINT fk_movimientoCaja_usuario FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario)
            );''',
            '''CREATE TABLE IF NOT EXISTS PedidoVenta(
                idPedidoVenta SERIAL PRIMARY KEY,
                fechaPedido TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                totalPedido NUMERIC(10,2) NOT NULL DEFAULT 0,
                Usuario_idUsuario INT NOT NULL,
                Mesa_idMesa INT NOT NULL,
                EstadoPedido_idEstado INT NOT NULL,
                TipoPedido_idTipoPedido INT NOT NULL,
                CONSTRAINT fk_pedido_usuario FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario),
                CONSTRAINT fk_pedido_mesa FOREIGN KEY (Mesa_idMesa) REFERENCES Mesa(idMesa),
                CONSTRAINT fk_pedido_estado FOREIGN KEY (EstadoPedido_idEstado) REFERENCES EstadoPedido(idEstado),
                CONSTRAINT fk_pedido_tipo FOREIGN KEY (TipoPedido_idTipoPedido) REFERENCES TipoPedido(idTipoPedido)
            );''',
            
            # --- TABLAS DE DETALLE Y FACTURACIÓN ---
            '''CREATE TABLE IF NOT EXISTS DetallePedidoVenta(
                idDetallePedidoVenta SERIAL PRIMARY KEY,
                cantidad INT NOT NULL,
                precioUnitario NUMERIC(10,2) NOT NULL,
                subtotal NUMERIC(10,2) NOT NULL,
                PedidoVenta_idPedidoVenta INT NOT NULL,
                Productos_idProductos INT NOT NULL,
                CONSTRAINT fk_detalle_pedido FOREIGN KEY (PedidoVenta_idPedidoVenta) REFERENCES PedidoVenta(idPedidoVenta),
                CONSTRAINT fk_detalle_producto FOREIGN KEY (Productos_idProductos) REFERENCES Productos(idProductos)
            );''',
            '''CREATE TABLE IF NOT EXISTS CabeceraRecibo(
                idCabeceraRecibo SERIAL PRIMARY KEY,
                numeroRecibo VARCHAR(30) NOT NULL,
                fechaEmision TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                totalGeneral NUMERIC(10,2) NOT NULL,
                PedidoVenta_idPedidoVenta INT NOT NULL,
                EstadoRecibo_idEstadoRecibo INT NOT NULL,
                MetodoPago_idMetodoPago INT NOT NULL,
                AperturaCierreCaja_idAperturaCierreCaja INT NOT NULL,
                CONSTRAINT fk_recibo_pedido FOREIGN KEY (PedidoVenta_idPedidoVenta) REFERENCES PedidoVenta(idPedidoVenta),
                CONSTRAINT fk_recibo_estado FOREIGN KEY (EstadoRecibo_idEstadoRecibo) REFERENCES EstadoRecibo(idEstadoRecibo),
                CONSTRAINT fk_recibo_metodo FOREIGN KEY (MetodoPago_idMetodoPago) REFERENCES MetodoPago(idMetodoPago),
                CONSTRAINT fk_recibo_apertura FOREIGN KEY (AperturaCierreCaja_idAperturaCierreCaja) REFERENCES AperturaCierreCaja(idAperturaCierreCaja)
            );''',
            '''CREATE TABLE IF NOT EXISTS CuerpoRecibo(
                idCuerpoRecibo SERIAL PRIMARY KEY,
                CabeceraRecibo_idCabeceraRecibo INT NOT NULL,
                DetallePedidoVenta_idDetallePedidoVenta INT NOT NULL,
                CONSTRAINT fk_cuerpo_cabecera FOREIGN KEY (CabeceraRecibo_idCabeceraRecibo) REFERENCES CabeceraRecibo(idCabeceraRecibo),
                CONSTRAINT fk_cuerpo_detalle FOREIGN KEY (DetallePedidoVenta_idDetallePedidoVenta) REFERENCES DetallePedidoVenta(idDetallePedidoVenta)
            );'''
        ]

        for tabla in tablas:
            cursor.execute(tabla)
            
        conexion.commit()
        print("Estructura de tablas de Chicken Biker desplegada con éxito en Postgres.")
        cursor.close()
        conexion.close()
    except Exception as e:
        print(f"Error al crear el esquema: {e}")