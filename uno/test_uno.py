import unittest
from parameterized import parameterized
from .const import RED, YELLOW, GREEN
from .card import (
    NumberCard,
    ReverseCard,
    WildCard,
    SkipCard,
    DrawFourCard,
    DrawTwoCard,
)


class TestUno(unittest.TestCase):

    @parameterized.expand([
        (SkipCard(RED), NumberCard(RED, '1')),
        (SkipCard(RED), SkipCard(RED)),
        (SkipCard(RED), ReverseCard(RED)),
        (SkipCard(RED), DrawTwoCard(RED)),
        (ReverseCard(RED), NumberCard(RED, '1')),
        (ReverseCard(RED), SkipCard(RED)),
        (ReverseCard(RED), ReverseCard(RED)),
        (ReverseCard(RED), DrawTwoCard(RED)),
        (DrawTwoCard(RED), NumberCard(RED, '1')),
        (DrawTwoCard(RED), SkipCard(RED)),
        (DrawTwoCard(RED), ReverseCard(RED)),
        (DrawTwoCard(RED), DrawTwoCard(RED)),
        (NumberCard(RED, '0'), NumberCard(RED, '1')),
        (NumberCard(RED, '0'), SkipCard(RED)),
        (NumberCard(RED, '0'), ReverseCard(RED)),
        (NumberCard(RED, '0'), DrawTwoCard(RED)),
    ])
    def test_same_color_valid_color_to_colored_card(
        self,
        selected_card,
        top_card
    ):
        self.assertTrue(selected_card.same_color(top_card))

    @parameterized.expand([
        (SkipCard(RED), WildCard()),
        (SkipCard(RED), DrawFourCard()),
        (ReverseCard(RED), WildCard()),
        (ReverseCard(RED), DrawFourCard()),
        (DrawTwoCard(RED), WildCard()),
        (DrawTwoCard(RED), DrawFourCard()),
        (NumberCard(RED, '0'), WildCard()),
        (NumberCard(RED, '0'), DrawFourCard()),
    ])
    def test_same_color_valid_color_to_postcolored_card(
        self,
        selected_card,
        top_card
    ):
        top_card.set_color(RED)
        self.assertTrue(selected_card.same_color(top_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(YELLOW, '1')),
        (SkipCard(RED), SkipCard(YELLOW)),
        (SkipCard(RED), ReverseCard(YELLOW)),
        (SkipCard(RED), DrawTwoCard(YELLOW)),
        (ReverseCard(RED), NumberCard(YELLOW, '1')),
        (ReverseCard(RED), SkipCard(YELLOW)),
        (ReverseCard(RED), ReverseCard(YELLOW)),
        (ReverseCard(RED), DrawTwoCard(YELLOW)),
        (DrawTwoCard(RED), NumberCard(YELLOW, '1')),
        (DrawTwoCard(RED), SkipCard(YELLOW)),
        (DrawTwoCard(RED), ReverseCard(YELLOW)),
        (DrawTwoCard(RED), DrawTwoCard(YELLOW)),
        (NumberCard(RED, '0'), NumberCard(YELLOW, '1')),
        (NumberCard(RED, '0'), SkipCard(YELLOW)),
        (NumberCard(RED, '0'), ReverseCard(YELLOW)),
        (NumberCard(RED, '0'), DrawTwoCard(YELLOW)),
    ])
    def test_same_color_invalid_color_to_colored_card(
        self,
        top_card,
        selected_card,
    ):
        self.assertFalse(top_card.same_color(selected_card))

    @parameterized.expand([
        (SkipCard(RED), WildCard()),
        (SkipCard(RED), DrawFourCard()),
        (ReverseCard(RED), WildCard()),
        (ReverseCard(RED), DrawFourCard()),
        (DrawTwoCard(RED), WildCard()),
        (DrawTwoCard(RED), DrawFourCard()),
        (NumberCard(RED, '0'), WildCard()),
        (NumberCard(RED, '0'), DrawFourCard()),
    ])
    def test_same_color_invalid_color_to_postcolored_card(
        self,
        selected_card,
        top_card
    ):
        top_card.set_color(YELLOW)
        self.assertFalse(selected_card.same_color(top_card))

    @parameterized.expand([
        (SkipCard(RED), SkipCard(GREEN)),
        (ReverseCard(RED), ReverseCard(GREEN)),
        (DrawTwoCard(RED), DrawTwoCard(GREEN)),
    ])
    def test_same_type_valid_colored_cards(self, selected_card, top_card):
        self.assertTrue(selected_card.same_type(top_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(GREEN, '1')),
        (SkipCard(RED), ReverseCard(GREEN)),
        (SkipCard(RED), DrawTwoCard(GREEN)),
        (ReverseCard(RED), NumberCard(GREEN, '1')),
        (ReverseCard(RED), SkipCard(GREEN)),
        (ReverseCard(RED), DrawTwoCard(GREEN)),
        (DrawTwoCard(RED), NumberCard(GREEN, '1')),
        (DrawTwoCard(RED), SkipCard(GREEN)),
        (DrawTwoCard(RED), ReverseCard(GREEN)),
        (NumberCard(RED, '0'), SkipCard(GREEN)),
        (NumberCard(RED, '0'), ReverseCard(GREEN)),
        (NumberCard(RED, '0'), DrawTwoCard(GREEN)),
    ])
    def test_same_type_invalid_colored_cards(self, selected_card, top_card):
        self.assertFalse(selected_card.same_type(top_card))

    @parameterized.expand([
        ('0',),
        ('1',),
        ('2',),
        ('3',),
        ('4',),
        ('5',),
        ('6',),
        ('7',),
        ('8',),
        ('9',),
    ])
    def test_same_number_valid_number_to_number_card(self, number):
        selected_card = NumberCard(RED, number)
        top_card = NumberCard(YELLOW, number)
        self.assertTrue(selected_card.same_number(top_card))

    @parameterized.expand([
        ('0', '1'),
        ('2', '3'),
        ('4', '5'),
        ('6', '7'),
        ('8', '9'),
    ])
    def test_same_number_invalid_number_to_number_card(self, number1, number2):
        selected_card = NumberCard(RED, number1)
        top_card = NumberCard(YELLOW, number2)
        self.assertFalse(selected_card.same_number(top_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(RED, '1')),
        (SkipCard(RED), SkipCard(YELLOW)),
        (SkipCard(RED), ReverseCard(RED)),
        (SkipCard(RED), DrawTwoCard(RED)),
        (ReverseCard(RED), NumberCard(RED, '1')),
        (ReverseCard(RED), SkipCard(RED)),
        (ReverseCard(RED), ReverseCard(YELLOW)),
        (ReverseCard(RED), DrawTwoCard(RED)),
        (DrawTwoCard(RED), NumberCard(RED, '1')),
        (DrawTwoCard(RED), SkipCard(RED)),
        (DrawTwoCard(RED), ReverseCard(RED)),
        (DrawTwoCard(RED), DrawTwoCard(YELLOW)),
        (NumberCard(RED, '0'), NumberCard(YELLOW, '0')),
        (NumberCard(RED, '0'), NumberCard(RED, '1')),
        (NumberCard(RED, '0'), SkipCard(RED)),
        (NumberCard(RED, '0'), ReverseCard(RED)),
        (NumberCard(RED, '0'), DrawTwoCard(RED)),
    ])
    def test_is_valid_from_colored_card_to_valid_colored_card(
        self,
        selected_card,
        top_card
    ):
        self.assertTrue(selected_card.is_valid(top_card))

    @parameterized.expand([
        (SkipCard(RED), WildCard()),
        (SkipCard(RED), DrawFourCard()),
        (ReverseCard(RED), WildCard()),
        (ReverseCard(RED), DrawFourCard()),
        (DrawTwoCard(RED), WildCard()),
        (DrawTwoCard(RED), DrawFourCard()),
        (NumberCard(RED, '0'), WildCard()),
        (NumberCard(RED, '0'), DrawFourCard()),
    ])
    def test_is_valid_from_colored_card_to_valid_postcolored_card(
        self,
        selected_card,
        top_card
    ):
        top_card.set_color(RED)
        self.assertTrue(selected_card.is_valid(top_card))

    @parameterized.expand([
        (SkipCard(RED), NumberCard(YELLOW, '1')),
        (SkipCard(RED), ReverseCard(YELLOW)),
        (SkipCard(RED), DrawTwoCard(YELLOW)),
        (ReverseCard(RED), NumberCard(YELLOW, '1')),
        (ReverseCard(RED), SkipCard(YELLOW)),
        (ReverseCard(RED), DrawTwoCard(YELLOW)),
        (DrawTwoCard(RED), NumberCard(YELLOW, '1')),
        (DrawTwoCard(RED), SkipCard(YELLOW)),
        (DrawTwoCard(RED), ReverseCard(YELLOW)),
        (NumberCard(RED, '0'), NumberCard(YELLOW, '1')),
        (NumberCard(RED, '0'), SkipCard(YELLOW)),
        (NumberCard(RED, '0'), ReverseCard(YELLOW)),
        (NumberCard(RED, '0'), DrawTwoCard(YELLOW)),
    ])
    def test_is_valid_from_colored_card_to_invalid_colored_card(
        self,
        top_card,
        selected_card,
    ):
        self.assertFalse(top_card.is_valid(selected_card))

    @parameterized.expand([
        (SkipCard(RED), WildCard()),
        (SkipCard(RED), DrawFourCard()),
        (ReverseCard(RED), WildCard()),
        (ReverseCard(RED), DrawFourCard()),
        (DrawTwoCard(RED), WildCard()),
        (DrawTwoCard(RED), DrawFourCard()),
        (NumberCard(RED, '0'), WildCard()),
        (NumberCard(RED, '0'), DrawFourCard()),
    ])
    def test_is_valid_from_colored_card_to_invalid_postcolored_card(
        self,
        selected_card,
        top_card
    ):
        top_card.set_color(YELLOW)
        self.assertFalse(selected_card.is_valid(top_card))

    @parameterized.expand([
        (DrawFourCard(), NumberCard(RED, '1')),
        (DrawFourCard(), SkipCard(RED)),
        (DrawFourCard(), ReverseCard(RED)),
        (DrawFourCard(), DrawTwoCard(RED)),
        (DrawFourCard(), DrawFourCard()),
        (DrawFourCard(), WildCard()),
        (WildCard(), NumberCard(RED, '1')),
        (WildCard(), SkipCard(RED)),
        (WildCard(), ReverseCard(RED)),
        (WildCard(), DrawTwoCard(RED)),
        (WildCard(), DrawFourCard()),
        (WildCard(), WildCard()),
    ])
    def test_is_valid_postcolored_card_to_any_card(
        self,
        selected_card,
        top_card
    ):
        self.assertTrue(selected_card.is_valid(top_card))
