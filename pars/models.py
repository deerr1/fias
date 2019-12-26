from django.db import models


class NormativeDocumentType(models.Model):
    NDTYPEID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=250,blank=True)
    
    def __str__(self):
        return str(self.NDTYPEID)

class NormativeDocument(models.Model):
    NORMDOCID=models.CharField(max_length=36,blank=True,primary_key=True)
    DOCNAME=models.CharField(max_length=500,blank=True)
    DOCDATE=models.DateField(null=True,blank=True)
    DOCNUM=models.CharField(max_length=20,blank=True)
    DOCTYPE=models.ForeignKey(NormativeDocumentType)
    DOCIMGID=models.CharField(max_length=36,blank=True)

    def __str__(self):
        return str(self.NORMDOCID)

class DelNormativeDocument(models.Model):
    NORMDOCID=models.CharField(max_length=36,blank=True,primary_key=True)
    DOCNAME=models.CharField(max_length=500,blank=True)
    DOCDATE=models.DateField(null=True,blank=True)
    DOCNUM=models.CharField(max_length=20,blank=True)
    DOCTYPE=models.ForeignKey(NormativeDocumentType)
    DOCIMGID=models.CharField(max_length=36,blank=True)

    def __str__(self):
        return str(self.NORMDOCID)

class AddressObjectTypeLEVEL(models.Model):
    LEVEL=models.IntegerField(blank=True,primary_key=True)
    SCNAME=models.CharField(max_length=10,blank=True)
    SOCRNAME=models.CharField(max_length=50,blank=True)
    KOD_T_ST=models.CharField(max_length=4,blank=True)

    def __str__(self):
        return str(self.LEVEL)

class ActualStatus(models.Model):
    ACTSTATID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.ACTSTATID)

class CenterStatus(models.Model):
    CENTERSTID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.CENTERSTID)

class CurrentStatus(models.Model):
    CURENTSTID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.CURENTSTID)

class OperationStatus(models.Model):
    OPERSTATID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.OPERSTATID)

class Stead(models.Model):
    STEADGUID=models.CharField(max_length=36,blank=True)
    NUMBER=models.CharField(max_length=120,blank=True)
    REGIONCODE=models.CharField(max_length=2,blank=True)
    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=11,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    PARENTGUID=models.CharField(max_length=36,blank=True)
    STEADID=models.CharField(max_length=36,blank=True,primary_key=True)
    PREVID=models.CharField(max_length=36,blank=True)
    NEXTID=models.CharField(max_length=36,blank=True)
    OPERSTATUS=models.ForeignKey(OperationStatus)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    NORMDOC=models.ForeignKey(NormativeDocument)
    LIVESTATUS=models.CharField(max_length=3,blank=True)
    CADNUM=models.CharField(max_length=100,blank=True)
    DIVTYPE=models.IntegerField(blank=True)

    def __str__(self):
        return str(self.STEADID)

class EstateStatus(models.Model):
    ESTSTATID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=20,blank=True)
    SHORTNAME=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return str(self.ESTSTATID)

class StructureStatus(models.Model):
    STRSTATID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=20,blank=True)
    SHORTNAME=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return str(self.STRSTATID)

class HouseStateStatus(models.Model):
    HOUSESTID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=60,blank=True)

    def __str__(self):
        return str(self.HOUSESTID)

class IntervalStatus(models.Model):
    INTVSTATID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=60,blank=True)

    def __str__(self):
        return str(self.INTVSTATID)

class FlatType(models.Model):
    FLTYPEID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=20,blank=True)
    SHORTNAME=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return str(self.FLTYPEID)

class RoomType(models.Model):
    RMTYPEID=models.IntegerField(blank=True,primary_key=True)
    NAME=models.CharField(max_length=20,blank=True)
    SHORTNAME=models.CharField(max_length=20,blank=True)

    def __str__(self):
        return str(self.RMTYPEID)

class Room(models.Model):
    ROOMGUID=models.CharField(max_length=36,blank=True)
    FLATNUMBER=models.CharField(max_length=50,blank=True)
    FLATTYPE=models.ForeignKey(FlatType)
    ROOMNUMBER=models.CharField(max_length=50,blank=True)
    ROOMTYPE=models.ForeignKey(RoomType)
    REGIONCODE=models.CharField(max_length=2,blank=True)
    POSTALCODE=models.CharField(max_length=6,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    HOUSEGUID=models.CharField(max_length=36,blank=True)
    ROOMID=models.CharField(max_length=36,blank=True,primary_key=True)
    PREVID=models.CharField(max_length=36,blank=True)
    NEXTID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    LIVESTATUS=models.CharField(max_length=3,blank=True)
    NORMDOC=models.ForeignKey(NormativeDocument)
    OPERSTATUS=models.ForeignKey(OperationStatus)
    CADNUM=models.CharField(max_length=100,blank=True)
    ROOMCADNUM=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.ROOMID)


class Adress(models.Model):
    AOGUID = models.CharField(max_length=36,blank=True)
    FORMALNAME = models.CharField(max_length=120,blank=True)
    REGIONCODE = models.CharField(max_length=2,blank=True)
    AUTOCODE = models.CharField(max_length=1,blank=True)
    AREACODE = models.CharField(max_length=3,blank=True)
    CITYCODE = models.CharField(max_length=3,blank=True)
    CTARCODE = models.CharField(max_length=3,blank=True)
    PLACECODE = models.CharField(max_length=3,blank=True)
    PLANCODE = models.CharField(max_length=4,blank=True)
    STREETCODE = models.CharField(max_length=4,blank=True)
    EXTRCODE = models.CharField(max_length=4,blank=True)
    SEXTCODE = models.CharField(max_length=3,blank=True)
    OFFNAME = models.CharField(max_length=120,blank=True)
    POSTALCODE = models.CharField(max_length=6,blank=True)
    IFNSFL = models.CharField(max_length=4,blank=True)
    TERRIFNSFL = models.CharField(max_length=4,blank=True)
    IFNSUL = models.CharField(max_length=4,blank=True)
    TERRIFNSUL = models.CharField(max_length=4,blank=True)
    OKATO = models.CharField(max_length=11,blank=True)
    OKTMO = models.CharField(max_length=11,blank=True)
    UPDATEDATE = models.DateField(null=True,blank=True)
    SHORTNAME = models.CharField(max_length=10,blank=True)
    AOLEVEL = models.ForeignKey(AddressObjectTypeLEVEL)
    PARENTGUID = models.CharField(max_length=36,blank=True)
    AOID = models.CharField(max_length=36,blank=True,primary_key=True)
    PREVID = models.CharField(max_length=36,blank=True)
    NEXTID = models.CharField(max_length=36,blank=True)
    CODE = models.CharField(max_length=17,blank=True)
    PLAINCODE = models.CharField(max_length=15,blank=True)
    ACTSTATUS = models.ForeignKey(ActualStatus)
    CENTSTATUS = models.ForeignKey(CenterStatus)
    OPERSTATUS = models.ForeignKey(OperationStatus)
    CURRSTATUS = models.ForeignKey(CurrentStatus)
    STARTDATE = models.DateField(null=True,blank=True)
    ENDDATE = models.DateField(null=True,blank=True)
    NORMDOC = models.ForeignKey(NormativeDocument)
    LIVESTATUS = models.CharField(max_length=3,blank=True)
    DIVTYPE = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.AOID)

class DelAdress(models.Model):
    AOGUID = models.CharField(max_length=36,blank=True)
    FORMALNAME = models.CharField(max_length=120,blank=True)
    REGIONCODE = models.CharField(max_length=2,blank=True)
    AUTOCODE = models.CharField(max_length=1,blank=True)
    AREACODE = models.CharField(max_length=3,blank=True)
    CITYCODE = models.CharField(max_length=3,blank=True)
    CTARCODE = models.CharField(max_length=3,blank=True)
    PLACECODE = models.CharField(max_length=3,blank=True)
    PLANCODE = models.CharField(max_length=4,blank=True)
    STREETCODE = models.CharField(max_length=4,blank=True)
    EXTRCODE = models.CharField(max_length=4,blank=True)
    SEXTCODE = models.CharField(max_length=3,blank=True)
    OFFNAME = models.CharField(max_length=120,blank=True)
    POSTALCODE = models.CharField(max_length=6,blank=True)
    IFNSFL = models.CharField(max_length=4,blank=True)
    TERRIFNSFL = models.CharField(max_length=4,blank=True)
    IFNSUL = models.CharField(max_length=4,blank=True)
    TERRIFNSUL = models.CharField(max_length=4,blank=True)
    OKATO = models.CharField(max_length=11,blank=True)
    OKTMO = models.CharField(max_length=11,blank=True)
    UPDATEDATE = models.DateField(null=True,blank=True)
    SHORTNAME = models.CharField(max_length=10,blank=True)
    AOLEVEL = models.ForeignKey(AddressObjectTypeLEVEL)
    PARENTGUID = models.CharField(max_length=36,blank=True)
    AOID = models.CharField(max_length=36,blank=True,primary_key=True)
    PREVID = models.CharField(max_length=36,blank=True)
    NEXTID = models.CharField(max_length=36,blank=True)
    CODE = models.CharField(max_length=17,blank=True)
    PLAINCODE = models.CharField(max_length=15,blank=True)
    ACTSTATUS = models.ForeignKey(ActualStatus)
    CENTSTATUS = models.ForeignKey(CenterStatus)
    OPERSTATUS = models.ForeignKey(OperationStatus)
    CURRSTATUS = models.ForeignKey(CurrentStatus)
    STARTDATE = models.DateField(null=True,blank=True)
    ENDDATE = models.DateField(null=True,blank=True)
    NORMDOC = models.ForeignKey(NormativeDocument)
    LIVESTATUS = models.CharField(max_length=3,blank=True)


    def __str__(self):
        return str(self.AOID)

class House(models.Model):

    POSTALCODE=models.CharField(max_length=6,blank=True)
    REGIONCODE=models.CharField(max_length=2,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=4,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    HOUSENUM=models.CharField(max_length=20,blank=True)
    ESTSTATUS=models.ForeignKey(EstateStatus)
    BUILDNUM=models.CharField(max_length=10,blank=True)
    STRUCNUM=models.CharField(max_length=10,blank=True)
    STRSTATUS=models.ForeignKey(StructureStatus)
    HOUSEID=models.CharField(max_length=36,blank=True,primary_key=True)
    HOUSEGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    STATSTATUS=models.ForeignKey(HouseStateStatus)
    NORMDOC=models.ForeignKey(NormativeDocument)
    COUNTER=models.IntegerField(blank=True)
    CADNUM=models.CharField(max_length=100,blank=True)
    DIVTYPE=models.IntegerField(blank=True)

    def __str__(self):
        return str(self.HOUSEID)

class DelHouse(models.Model):

    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=4,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    HOUSENUM=models.CharField(max_length=20,blank=True)
    ESTSTATUS=models.ForeignKey(EstateStatus)
    BUILDNUM=models.CharField(max_length=10,blank=True)
    STRUCNUM=models.CharField(max_length=10,blank=True)
    STRSTATUS=models.ForeignKey(StructureStatus)
    HOUSEID=models.CharField(max_length=36,blank=True,primary_key=True)
    HOUSEGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    STATSTATUS=models.ForeignKey(HouseStateStatus)
    NORMDOC=models.ForeignKey(NormativeDocument)
    COUNTER=models.IntegerField(blank=True)
    CADNUM=models.CharField(max_length=100,blank=True)
    DIVTYPE=models.IntegerField(blank=True)

    def __str__(self):
        return str(self.HOUSEID)

class HouseInterval(models.Model):
    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=11,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    INTSTART=models.IntegerField(blank=True)
    INTEND=models.IntegerField(blank=True)
    HOUSEINTID=models.CharField(max_length=36,blank=True,primary_key=True)
    INTGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    INTSTATUS=models.ForeignKey(IntervalStatus)
    NORMDOC=models.ForeignKey(NormativeDocument)
    COUNTER=models.IntegerField(blank=True)

    def __str__(self):
        return str(self.HOUSEINTID)

class DelHouseInterval(models.Model):
    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=11,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    INTSTART=models.IntegerField(blank=True)
    INTEND=models.IntegerField(blank=True)
    HOUSEINTID=models.CharField(max_length=36,blank=True,primary_key=True)
    INTGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    INTSTATUS=models.ForeignKey(IntervalStatus)
    NORMDOC=models.ForeignKey(NormativeDocument)
    COUNTER=models.IntegerField(blank=True)

    def __str__(self):
        return str(self.HOUSEINTID)

class Landmark(models.Model):
    LOCATION=models.CharField(max_length=500,blank=True)
    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=11,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    LANDID=models.CharField(max_length=36,blank=True,primary_key=True)
    LANDGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    NORMDOC=models.ForeignKey(NormativeDocument)

    def __str__(self):
        return str(self.LANDID)

class DelLandmark(models.Model):
    LOCATION=models.CharField(max_length=500,blank=True)
    POSTALCODE=models.CharField(max_length=6,blank=True)
    IFNSFL=models.CharField(max_length=4,blank=True)
    TERRIFNSFL=models.CharField(max_length=4,blank=True)
    IFNSUL=models.CharField(max_length=4,blank=True)
    TERRIFNSUL=models.CharField(max_length=4,blank=True)
    OKATO=models.CharField(max_length=11,blank=True)
    OKTMO=models.CharField(max_length=11,blank=True)
    UPDATEDATE=models.DateField(null=True,blank=True)
    LANDID=models.CharField(max_length=36,blank=True,primary_key=True)
    LANDGUID=models.CharField(max_length=36,blank=True)
    AOGUID=models.CharField(max_length=36,blank=True)
    STARTDATE=models.DateField(null=True,blank=True)
    ENDDATE=models.DateField(null=True,blank=True)
    NORMDOC=models.ForeignKey(NormativeDocument)

    def __str__(self):
        return str(self.LANDID)


    
