from django.urls import path
from study.apps import StudyConfig
from study.views import StudyListView, StudyDetailView, StudyUpdateView, StudyCreateView, StudyDeleteView, \
    MaterialsListView, MaterialsDetailView, MaterialsUpdateView, MaterialsCreateView, MaterialsDeleteView, \
    TestCreateAPIView, QuestionListCreateAPIView, AnswerListCreateAPIView, TestUpdateAPIView, TestDeleteAPIView

app_name = StudyConfig.name

urlpatterns = [
    path('study/', StudyListView.as_view(), name='study_list'),
    path('study/<int:pk>/', StudyDetailView.as_view(), name='study_detail'),
    path('study/create/', StudyCreateView.as_view(), name='study_create'),
    path('study/update/<int:pk>/', StudyUpdateView.as_view(), name='study_update'),
    path('study/delete/<int:pk>/', StudyDeleteView.as_view(), name='study_delete'),
    path('materials/', MaterialsListView.as_view(), name='materials_list'),
    path('materials/<int:pk>/', MaterialsDetailView.as_view(), name='materials_detail'),
    path('materials/create/', MaterialsCreateView.as_view(), name='materials_create'),
    path('materials/update/<int:pk>/', MaterialsUpdateView.as_view(), name='materials_update'),
    path('materials/delete/<int:pk>/', MaterialsDeleteView.as_view(), name='materials_delete'),
    path('tests/create/', TestCreateAPIView.as_view(), name='create_test'),
    path('tests/update/<int:pk>/', TestUpdateAPIView.as_view(), name='update_test'),
    path('tests/delete/<int:pk>/', TestDeleteAPIView.as_view(), name='delete_test'),
    path('questions/create/', QuestionListCreateAPIView.as_view(), name='create_question'),
    path('answers/create/', AnswerListCreateAPIView.as_view(), name='create_answer'),
]
