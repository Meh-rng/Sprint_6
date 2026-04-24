import pytest
from pages.home_page import HomePage
from data.faq_data import faq_questions_data


class TestFaq:
    @pytest.mark.parametrize("question_index, expected_text", faq_questions_data)
    def test_faq_answers(self, driver, question_index, expected_text):
        home_page = HomePage(driver)
        home_page.click_question(question_index)
        actual_text = home_page.get_answer_text(question_index)
        assert expected_text in actual_text, f"Ответ на вопрос {question_index} не соответствует ожидаемому"