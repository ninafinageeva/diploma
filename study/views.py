from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from study.models import Study, Materials, Test, Question, Answer
from study.paginators import Pagination
from study.serializers import StudySerializer, MaterialsSerializer, TestSerializer, QuestionSerializer, AnswerSerializer


class StudyListView(ListAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class StudyDetailView(RetrieveAPIView):
    """ Study list API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


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

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class StudyDeleteView(DestroyAPIView):
    """ Study delete API View """

    serializer_class = StudySerializer
    queryset = Study.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Study.objects.all()
        else:
            return Study.objects.filter(owner=user)


class MaterialsListView(ListAPIView):
    """ Materials list API View """

    serializer_class = MaterialsSerializer
    queryset = Materials.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]


class MaterialsDetailView(RetrieveAPIView):
    """ Materials retrieve API View """

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


class TestCreateAPIView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestUpdateAPIView(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDeleteAPIView(DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionListCreateAPIView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerListCreateAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

