import pytest
from pages.home_page import HomePage


class TestFaq:
    @pytest.mark.parametrize("question_index, expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат."),
        (2, "Допустим, вы оформляете заказ на 8 мая."),
        (3, "Только начиная с завтрашнего дня."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить."),
        (5, "Самокат приезжает к вам с полной зарядкой."),
        (6, "Да, пока самокат не привезли. Штрафа не будет."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_faq_answers(self, driver, question_index, expected_text):
        home_page = HomePage(driver)
        home_page.click_question(question_index)
        actual_text = home_page.get_answer_text(question_index)
        assert expected_text in actual_text
        