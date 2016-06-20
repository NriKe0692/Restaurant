from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

class RestauranteDjangoadminlog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'restaurante_djangoadminlog'

class RestauranteDjangomigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'restaurante_djangomigrations'

class TaDetalle(models.Model):
    idpedido = models.ForeignKey('TaPedido', models.DO_NOTHING, db_column='IDPEDIDO')  # Field name made lowercase.
    idplatillo = models.ForeignKey('TaPlatillo', models.DO_NOTHING, db_column='IDPLATILLO')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.
    precioparcial = models.DecimalField(db_column='PRECIOPARCIAL', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_detalle'
        unique_together = (('idpedido', 'idplatillo'),)

    def __unicode__(self):
        return self.unique_together

class TaEmpleado(models.Model):
    idusuario = models.ForeignKey('TaUsuario', models.DO_NOTHING, db_column='IDUSUARIO')  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=40)  # Field name made lowercase.
    idempleado = models.IntegerField(db_column='IDEMPLEADO', primary_key=True)
    apellido = models.CharField(db_column='APELLIDO', max_length=40)  # Field name made lowercase.
    dni = models.IntegerField(db_column='DNI')  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_empleado'

    def __unicode__(self):
        return self.nombre+" "+self.apellido

class TaEstadoPedido(models.Model):
    idestadopedido = models.IntegerField(db_column='IDESTADOPEDIDO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_estado_pedido'

    def __unicode__(self):
        return self.nombre

class TaFormaPago(models.Model):
    idformapago = models.IntegerField(db_column='IDFORMAPAGO', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_forma_pago'

    def __unicode__(self):
        return self.nombre

class TaMesa(models.Model):
    idmesa = models.IntegerField(db_column='IDMESA', primary_key=True)  # Fieldname made lowercase.
    numero = models.IntegerField(db_column='NUMERO')  # Field name made lowercase.
    piso = models.IntegerField(db_column='PISO')  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_mesa'

    def __unicode__(self):
        return self.numero

class TaMesaPedido(models.Model):
    idmesa = models.ForeignKey(TaMesa, models.DO_NOTHING, db_column='IDMESA')  # Field name made lowercase.
    idpedido = models.ForeignKey('TaPedido', models.DO_NOTHING, db_column='IDPEDIDO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_mesa_pedido'
        unique_together = (('idmesa', 'idpedido'),)

class TaPedido(models.Model):
    idpedido = models.IntegerField(db_column='IDPEDIDO', primary_key=True)  # Field name made lowercase.
    idformapago = models.ForeignKey(TaFormaPago, models.DO_NOTHING, db_column='IDFORMAPAGO')  # Field name made lowercase.
    idestadopedido = models.ForeignKey(TaEstadoPedido, models.DO_NOTHING, db_column='IDESTADOPEDIDO')  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')  # Field name made lowercase.
    montototal = models.DecimalField(db_column='MONTOTOTAL', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_pedido'

    def __unicode__(self):
        return self.idpedido

class TaPedidoUsuario(models.Model):
    idpedido = models.ForeignKey(TaPedido, models.DO_NOTHING, db_column='IDPEDIDO')  # Field name made lowercase.
    idusuario = models.ForeignKey('TaUsuario', models.DO_NOTHING, db_column='IDUSUARIO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_pedido_usuario'
        unique_together = (('idusuario', 'idpedido'),)

class TaEstadoPlatillo(models.Model):
    idestadoplatillo = models.IntegerField(db_column='IDESTADOPLATILLO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_estado_platillo'

    def __unicode__(self):
        return self.nombre

class TaPlatillo(models.Model):
    idplatillo = models.IntegerField(db_column='IDPLATILLO', primary_key=True)
    nombre = models.CharField(db_column='NOMBRE', max_length=45)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=5, decimal_places=2)  # Field name made lowercase.
    idtipoplatillo = models.ForeignKey('TaTipoPlatillo', models.DO_NOTHING, db_column='IDTIPOPLATILLO')  # Field name made lowercase.
    idestadoplatillo = models.ForeignKey(TaEstadoPlatillo, models.DO_NOTHING, db_column='IDESTADOPLATILLO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_platillo'

    def __unicode__(self):
        return self.nombre

class TaRol(models.Model):
    idrol = models.IntegerField(db_column='IDROL', primary_key=True, blank=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_rol'

    def __unicode__(self):
        return self.nombre

#ERROR EN TIPO PLATILLO 
class TaTipoPlatillo(models.Model):
    idtipoplatillo = models.IntegerField(db_column='IDTIPOPLATILLO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_tipo_platillo'

    def __unicode__(self):
        return self.nombre

class TaUsuario(models.Model):
    idusuario = models.CharField(db_column='IDUSUARIO', primary_key=True, max_length=30)  # Field name made lowercase.
    idrol = models.ForeignKey(TaRol, models.DO_NOTHING, db_column='IDROL')  # Field name made lowercase.
    clave = models.CharField(db_column='CLAVE', max_length=30)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ta_usuario'
    def __unicode__(self):
        return self.idusuario