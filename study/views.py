from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from study.models import Study, Materials
from study.paginators import Pagination
from study.serializers import StudySerializer, MaterialsSerializer


class StudyListView(ListAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]


class StudyDetailView(RetrieveAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]


class StudyCreateView(CreateAPIView):
    """ Study create API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]


class StudyUpdateView(UpdateAPIView):
    """ Study update API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]


class StudyDeleteView(DestroyAPIView):
    """ Study delete API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialsListView(ListAPIView):
    """ Materials list API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]


class MaterialsDetailView(RetrieveAPIView):
    """ Materials list API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialsCreateView(CreateAPIView):
    """ Materials create API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialsUpdateView(UpdateAPIView):
    """ Materials update API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialsDeleteView(DestroyAPIView):
    """ Materials delete API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    permission_classes = [IsAuthenticated]
