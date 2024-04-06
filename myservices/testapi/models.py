from django.db import models

# Model Table test
class TblTest(models.Model):
    id_tmu = models.AutoField(primary_key=True)
    username_tmu = models.CharField(max_length=100)
    password_tmu = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_tmu} - {self.username_tmu}"
    
    class Meta:
        managed = True
        db_table = 'tbl_m_user'