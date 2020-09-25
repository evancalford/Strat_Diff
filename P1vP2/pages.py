
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    form_model = 'player'
    def is_displayed(self):
        return self.subsession.round_number == 1
class DecisionPage(Page):
    form_model = 'player'
    form_fields = ['choice']
class MyWaitPage(WaitPage):
    after_all_players_arrive = 'determine_payoffs'
page_sequence = [MyPage, DecisionPage, MyWaitPage]