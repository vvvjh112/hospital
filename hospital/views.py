from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import NormalHSerializer,EmerHSerializer
from .models import NormalH
from .EmerH import Check_ID, Update_hospitalization, search_Emergency
from .aed import search_aed

#추가할 기능
#업데이트주기


#응급실운영하는 곳의 기관명과 좌표를 넘겨줌
class LocationList(APIView):
    def get(self, request):
        tests = NormalH.objects.filter(응급실운영여부 = "True")
        serializer = EmerHSerializer(tests, many=True)
        return Response(serializer.data)

class SearchEmergency(APIView):
    def get(self, request, lon, lat, format=None):
        data = search_Emergency(lon=lon, lat=lat)
        return Response(data)


#병원정보를 넘겨줌
class HospitalDetail(APIView):
    def get_objects(self,pk):
        # 병원 입원가용여부를 업데이트 후 오브젝트 반환
        # Update_hospitalization(Check_ID(pk))
        # a= Check_ID(pk)
        try:
            return NormalH.objects.filter(기관명 = pk)
        except NormalH.DoseNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_objects(pk)
        serializer = NormalHSerializer(list, many=True)
        return Response(serializer.data)

class SearchAed(APIView):
    def get(self, request, lon, lat, format=None):
        data = search_aed(lon=lon, lat=lat)
        return Response(data)

