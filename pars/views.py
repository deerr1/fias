from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .classes import *

# Create your views here.
def parse(request):

    import xml.sax
    import os

    def search(files,order):
        for xml in files:
            if xml.find(order)!=-1:
                return xml

    fil = os.path.abspath(__file__)
                
    
    fil = os.path.join(fil,'..\BD')
    fil = os.path.abspath(fil)
    os.chdir(path=fil)
    xml_files=os.listdir(os.getcwd())
    xml_order={
        'AS_NDOCTYPE':NormativeDocumentTypeObj(),
        'AS_NORMDOC':NormativeDocumentObj(),
        'AS_DEL_NORMDOC':DelNormativeDocumentObj(),
        'AS_SOCRBASE':AddressObjectTypeLEVELObj(),
        'AS_ACTSTAT':ActualStatusObj(),
        'AS_CENTERST':CenterStatusObj(),
        'AS_CURENTST':CurrentStatusObj(),
        'AS_OPERSTAT':OperationStatusObj(),
        'AS_STEAD':SteadObj(),
        'AS_ESTSTAT':EstateStatusObj(),
        'AS_STRSTAT':StructureStatusObj(),
        'AS_HSTSTAT':HouseStateStatusObj(),
        'AS_INTVSTAT':IntervalStatusObj(),
        'AS_FLATTYPE':FlatTypeObj(),
        'AS_ROOMTYPE':RoomTypeObj(),
        'AS_ROOM':RoomObj(),
        'AS_ADDROBJ':AdressObj(),
        'AS_DEL_ADDROBJ':DelAdressObj(),
        'AS_HOUSE':HouseObj(),
        'AS_DEL_HOUSE':DelHouseObj(),
    }

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    for xml in xml_order.keys():
        pat = search(xml_files,xml)

        Handler = xml_order.get(xml)
        
        parser.setContentHandler( Handler )    
        parser.parse(pat) 

    return HttpResponse(f"{xml_files}")
