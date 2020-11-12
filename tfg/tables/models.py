from django.db import models


class Registry(models.Model):
    AMB_T = models.DecimalField( max_digits=4, decimal_places=2)
    BOILER_T = models.DecimalField( max_digits=5, decimal_places=2)
    COOL_FLOW = models.DecimalField( max_digits=5, decimal_places=2)
    COOL_T_IN = models.DecimalField( max_digits=5, decimal_places=2)
    COOL_T_OUT = models.DecimalField( max_digits=5, decimal_places=2)
    CURRENT = models.DecimalField( max_digits=6, decimal_places=2)
    E_ENERGY = models.DecimalField( max_digits=6, decimal_places=1)
    E_POWER = models.DecimalField(max_digits=6, decimal_places=1)
    HEAD_T_SET = models.DecimalField( max_digits=6, decimal_places=2)
    HEAT_T_CON = models.DecimalField( max_digits=5, decimal_places=2)
    HRAT_T_LIM = models.DecimalField( max_digits=5, decimal_places=2)
    STATUS = models.SmallIntegerField()
    VDTTM = models.BigIntegerField()
    VOLTAGE = models.DecimalField( max_digits=5, decimal_places=2)
    DATETIME = models.DateTimeField()