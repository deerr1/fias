import xml.sax

from .models import *

class NormativeDocumentTypeObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.NDTYPEID= ""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="NormativeDocumentType":
            
            obj = NormativeDocumentType(**dict(attributes))
            obj.save()

class NormativeDocumentObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.NORMDOCID=""
        self.DOCNAME=""
        self.DOCDATE=""
        self.DOCNUM=""
        self.DOCTYPE=""
        self.DOCIMGID=""
    
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="NormativeDocument":
            attributes=dict(attributes)
            attributes["DOCTYPE"]=NormativeDocumentType.objects.get(NDTYPEID=attributes["DOCTYPE"])
            obj = NormativeDocument(**attributes)
            obj.save()

class DelNormativeDocumentObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.NORMDOCID=""
        self.DOCNAME=""
        self.DOCDATE=""
        self.DOCNUM=""
        self.DOCTYPE=""
        self.DOCIMGID=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="NormativeDocument":
            attributes=dict(attributes)
            attributes["DOCTYPE"]=NormativeDocumentType.objects.get(NDTYPEID=attributes["DOCTYPE"])
            obj = NormativeDocument(**attributes)
            obj.save()

class AddressObjectTypeLEVELObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.LEVEL=""
        self.SCNAME=""
        self.SOCRNAME=""
        self.KOD_T_ST=""
    
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="AddressObjectType":
            
            obj = AddressObjectTypeLEVEL(**dict(attributes))
            obj.save()

class ActualStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.ACTSTATID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="ActualStatus":
            
            obj = ActualStatus(**dict(attributes))
            obj.save()

class CenterStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.CENTERSTID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="CenterStatus":
            
            obj = CenterStatus(**dict(attributes))
            obj.save()

class CurrentStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.CURENTSTID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="CurrentStatus":
            
            obj = CurrentStatus(**dict(attributes))
            obj.save()

class OperationStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.OPERSTATID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="OperationStatus":
            
            obj = OperationStatus(**dict(attributes))
            obj.save()

class SteadObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.STEADGUID=""
        self.NUMBER=""
        self.REGIONCODE=""
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.PARENTGUID=""
        self.STEADID=""
        self.PREVID=""
        self.NEXTID=""
        self.OPERSTATUS=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.NORMDOC=""
        self.LIVESTATUS=""
        self.CADNUM=""
        self.DIVTYPE=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Stead":
            attributes=dict(attributes)
            attributes["OPERSTATUS"]=OperationStatus.objects.get(OPERSTATID=attributes["OPERSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(NORMDOCID=attributes["NORMDOC"])
            obj = Stead(**attributes)
            obj.save()

class EstateStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.ESTSTATID=""
        self.NAME=""
        self.SHORTNAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="EstateStatus":
            
            obj = EstateStatus(**dict(attributes))
            obj.save()

class StructureStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.STRSTATID=""
        self.NAME=""
        self.SHORTNAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="StructureStatus":
            
            obj = StructureStatus(**dict(attributes))
            obj.save()

class HouseStateStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.HOUSESTID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="HouseStateStatus":
            
            obj = HouseStateStatus(**dict(attributes))
            obj.save()

class IntervalStatusObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.INTVSTATID=""
        self.NAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="IntervalStatus":
            
            obj = IntervalStatus(**dict(attributes))
            obj.save()

class FlatTypeObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.FLTYPEID=""
        self.NAME=""
        self.SHORTNAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="FlatType":
            
            obj = FlatType(**dict(attributes))
            obj.save()

class RoomTypeObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.RMTYPEID=""
        self.NAME=""
        self.SHORTNAME=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="RoomType":
            
            obj = RoomType(**dict(attributes))
            obj.save()

class RoomObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.ROOMGUID=""
        self.FLATNUMBER=""
        self.FLATTYPE=""
        self.ROOMNUMBER=""
        self.ROOMTYPE=""
        self.REGIONCODE=""
        self.POSTALCODE=""
        self.UPDATEDATE=""
        self.HOUSEGUID=""
        self.ROOMID=""
        self.PREVID=""
        self.NEXTID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.LIVESTATUS=""
        self.NORMDOC=""
        self.OPERSTATUS=""
        self.CADNUM=""
        self.ROOMCADNUM=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Room":
            attributes=dict(attributes)
            attributes["FLATTYPE"]=FlatType.objects.get(attributes["FLATTYPE"])
            attributes["ROOMTYPE"]=RoomType.objects.get(attributes["ROOMTYPE"])
            obj = Room(**attributes)
            obj.save()

class HouseObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.POSTALCODE=""
        self.REGIONCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.HOUSENUM=""
        self.ESTSTATUS=""
        self.BUILDNUM=""
        self.STRUCNUM=""
        self.STRSTATUS=""
        self.HOUSEID=""
        self.HOUSEGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.STATSTATUS=""
        self.NORMDOC=""
        self.COUNTER=""
        self.CADNUM=""
        self.DIVTYPE=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="House":
            attributes=dict(attributes)
            attributes["ESTSTATUS"]=EstateStatus.objects.get(attributes["ESTSTATUS"])
            attributes["STRSTATUS"]=StructureStatus.objects.get(attributes["STRSTATUS"])
            attributes["STATSTATUS"]=HouseStateStatus.objects.get(attributes["STATSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = House(**attributes)
            obj.save()

class DelHouseObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.HOUSENUM=""
        self.ESTSTATUS=""
        self.BUILDNUM=""
        self.STRUCNUM=""
        self.STRSTATUS=""
        self.HOUSEID=""
        self.HOUSEGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.STATSTATUS=""
        self.NORMDOC=""
        self.COUNTER=""
        self.CADNUM=""
        self.DIVTYPE=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="House":
            attributes=dict(attributes)
            attributes["ESTSTATUS"]=EstateStatus.objects.get(attributes["ESTSTATUS"])
            attributes["STRSTATUS"]=StructureStatus.objects.get(attributes["STRSTATUS"])
            attributes["STATSTATUS"]=HouseStateStatus.objects.get(attributes["STATSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = House(**attributes)
            obj.save()

class HouseIntervalObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.INTSTART=""
        self.INTEND=""
        self.HOUSEINTID=""
        self.INTGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.INTSTATUS=""
        self.NORMDOC=""
        self.COUNTER=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="HouseInterval":
            attributes=dict(attributes)
            attributes["INTSTATUS"]=IntervalStatus.objects.get(attributes["INTSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = HouseInterval(**attributes)
            obj.save()

class DelHouseIntervalObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.INTSTART=""
        self.INTEND=""
        self.HOUSEINTID=""
        self.INTGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.INTSTATUS=""
        self.NORMDOC=""
        self.COUNTER=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="HouseInterval":
            attributes=dict(attributes)
            attributes["INTSTATUS"]=IntervalStatus.objects.get(attributes["INTSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = HouseInterval(**attributes)
            obj.save()

class LandmarkObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.LOCATION=""
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.LANDID=""
        self.LANDGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.NORMDOC=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Landmark":
            attributes=dict(attributes)
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = Landmark(**attributes)
            obj.save()

class DelLandmarkObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.LOCATION=""
        self.POSTALCODE=""
        self.IFNSFL=""
        self.TERRIFNSFL=""
        self.IFNSUL=""
        self.TERRIFNSUL=""
        self.OKATO=""
        self.OKTMO=""
        self.UPDATEDATE=""
        self.LANDID=""
        self.LANDGUID=""
        self.AOGUID=""
        self.STARTDATE=""
        self.ENDDATE=""
        self.NORMDOC=""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Landmark":
            
            attributes=dict(attributes)
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = Landmark(**attributes)
            obj.save()

class AdressObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.AOGUID = ""
        self.FORMALNAME = ""
        self.REGIONCODE = ""
        self.AUTOCODE = ""
        self.AREACODE = ""
        self.CITYCODE = ""
        self.CTARCODE = ""
        self.PLACECODE = ""
        self.PLANCODE = ""
        self.STREETCODE = ""
        self.EXTRCODE = ""
        self.SEXTCODE = ""
        self.OFFNAME = ""
        self.POSTALCODE = ""
        self.IFNSFL = ""
        self.TERRIFNSFL = ""
        self.IFNSUL = ""
        self.TERRIFNSUL = ""
        self.OKATO = ""
        self.OKTMO = ""
        self.UPDATEDATE = ""
        self.SHORTNAME = ""
        self.AOLEVEL = ""
        self.PARENTGUID = ""
        self.AOID = ""
        self.PREVID = ""
        self.NEXTID = ""
        self.CODE = ""
        self.PLAINCODE = ""
        self.ACTSTATUS = ""
        self.CENTSTATUS = ""
        self.OPERSTATUS = ""
        self.CURRSTATUS = ""
        self.STARTDATE = ""
        self.ENDDATE = ""
        self.NORMDOC = ""
        self.LIVESTATUS = ""
        self.DIVTYPE = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Object":
            attributes=dict(attributes)
            attributes["AOLEVEL"]=AddressObjectTypeLEVEL.objects.get(attributes["AOLEVEL"])
            attributes["ACTSTATUS"]=ActualStatus.objects.get(attributes["ACTSTATUS"])
            attributes["CENTSTATUS"]=CenterStatus.objects.get(attributes["CENTSTATUS"])
            attributes["OPERSTATUS"]=OperationStatus.objects.get(attributes["OPERSTATUS"])
            attributes["CURRSTATUS"]=CurrentStatus.objects.get(attributes["CURRSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = Adress(**attributes)
            obj.save()

class DelAdressObj( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.AOGUID = ""
        self.FORMALNAME = ""
        self.REGIONCODE = ""
        self.AUTOCODE = ""
        self.AREACODE = ""
        self.CITYCODE = ""
        self.CTARCODE = ""
        self.PLACECODE = ""
        self.PLANCODE = ""
        self.STREETCODE = ""
        self.EXTRCODE = ""
        self.SEXTCODE = ""
        self.OFFNAME = ""
        self.POSTALCODE = ""
        self.IFNSFL = ""
        self.TERRIFNSFL = ""
        self.IFNSUL = ""
        self.TERRIFNSUL = ""
        self.OKATO = ""
        self.OKTMO = ""
        self.UPDATEDATE = ""
        self.SHORTNAME = ""
        self.AOLEVEL = ""
        self.PARENTGUID = ""
        self.AOID = ""
        self.PREVID = ""
        self.NEXTID = ""
        self.CODE = ""
        self.PLAINCODE = ""
        self.ACTSTATUS = ""
        self.CENTSTATUS = ""
        self.OPERSTATUS = ""
        self.CURRSTATUS = ""
        self.STARTDATE = ""
        self.ENDDATE = ""
        self.NORMDOC = ""
        self.LIVESTATUS = ""
        self.DIVTYPE = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="Object":
            attributes=dict(attributes)
            attributes["AOLEVEL"]=AddressObjectTypeLEVEL.objects.get(attributes["AOLEVEL"])
            attributes["ACTSTATUS"]=ActualStatus.objects.get(attributes["ACTSTATUS"])
            attributes["CENTSTATUS"]=CenterStatus.objects.get(attributes["CENTSTATUS"])
            attributes["OPERSTATUS"]=OperationStatus.objects.get(attributes["OPERSTATUS"])
            attributes["CURRSTATUS"]=CurrentStatus.objects.get(attributes["CURRSTATUS"])
            attributes["NORMDOC"]=NormativeDocument.objects.get(attributes["NORMDOC"])
            obj = Adress(**attributes)
            obj.save()