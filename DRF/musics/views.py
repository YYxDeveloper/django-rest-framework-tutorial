# Create your views here.
from django.shortcuts import get_object_or_404
from musics.models import Music
# from musics.models import fun_raw_sql_query, fun_sql_cursor_update
from musics.serializers import MusicSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework.decorators import action

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    @action(methods=['get'], detail=True, permission_classes=[])
    def detailaa(self, request, pk=None):
        music = get_object_or_404(Music, pk=pk)
        result = {
            'singer': music.singer,
            'song': music.song
        }

        return Response(result, status=status.HTTP_200_OK)