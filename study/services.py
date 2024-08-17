from study.models import Question, Answer, Test
from users.models import User


def user_testing(user, test):
    # Получаем все вопросы для выбранного теста
    questions = Question.objects.filter(test=test)

    # Создаем словарь для хранения результатов тестирования
    test_results = {}

    # Проходимся по каждому вопросу
    for question in questions:
        # Получаем все ответы для текущего вопроса
        answers = Answer.objects.filter(question=question)

        # Выводим текст вопроса
        print(question.text)

        # Выводим все возможные ответы
        for answer in answers:
            print(answer.text)

        # Запрашиваем ответ у пользователя
        user_answer = input("Введите номер правильного ответа: ")

        # Проверяем правильность ответа и обновляем результаты тестирования
        if answers[int(user_answer) - 1].is_correct:
            print("Правильно!")
            test_results[question.text] = True
        else:
            print("Неправильно!")
            test_results[question.text] = False

    # Выводим результаты тестирования
    print("Результаты тестирования:")
    for question, result in test_results.items():
        print(f"{question}: {'Правильно' if result else 'Неправильно'}")


# Пример использования функции
# Предположим, что у нас есть пользователь user и тест test
user_instance = User.objects.get(id=1)
test_instance = Test.objects.get(id=1)

user_testing(user=user_instance, test=test_instance)
