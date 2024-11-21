from app_quiz.models import Question

def get_questions_by_theme(theme):
    """Возвращает все вопросы для выбранной темы."""
    questions = Question.objects.filter(theme=theme)
    return questions
