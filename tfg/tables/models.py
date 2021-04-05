from django.db import models
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'


class Registry(models.Model):
    AMB_T = models.DecimalField( max_digits=3, decimal_places=1)# not higher than 99.9
    BOILER_T = models.DecimalField( max_digits=4, decimal_places=1)# not higher than 999.9, should be under 100
    COOL_FLOW = models.DecimalField( max_digits=3, decimal_places=1)# l/min between 7-19, safe to assume not higher than 100
    COOL_T_IN = models.DecimalField( max_digits=4, decimal_places=1)# not higher than 999.9, should be under 100
    COOL_T_OUT = models.DecimalField( max_digits=4, decimal_places=1)# not higher than 999.9, should be under 100
    CURRENT = models.DecimalField( max_digits=3, decimal_places=2)# not higher than 5A, the nominal is 1000/230
    E_ENERGY = models.DecimalField( max_digits=5, decimal_places=1)# annual Kwh, not higher than 2300
    E_POWER = models.PositiveSmallIntegerField()# watts, not higher than 1000
    HEAT_T_CON = models.DecimalField( max_digits=5, decimal_places=1)# not higher than 999.9, should be under 100
    HEAT_T_LIM = models.DecimalField( max_digits=5, decimal_places=1)# not higher than 999.9, should be under 100
    STATUS = models.PositiveSmallIntegerField()# not higher than 32767, lower than 100, or than 1000 with errors
    VOLTAGE = models.DecimalField( max_digits=4, decimal_places=1)# not higher than 230
    DATETIME = models.DateTimeField()# datetime without milliseconds

