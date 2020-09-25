
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = 'This app is to collect the initial data on P1 v P2.'
class Constants(BaseConstants):
    name_in_url = 'P1vP2'
    players_per_group = 2
    num_rounds = 2
    description = ('P1 earns $20 if P1 and P2 choose different colours, and earns $5 if P1 and P2 choose the same colour. ', 'P2 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.', 'P1 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.', 'P2 earns $20 if P1 and P2 choose the same colour, and earns $5 if P1 and P2 choose different colours.')
    css_styles_template = 'P1vP2/css_styles.html'
class Subsession(BaseSubsession):
    P1_descr = models.LongStringField()
    P2_descr = models.LongStringField()
    payoff1 = models.StringField()
    payoff2 = models.StringField()
    title_descr = models.StringField()
    def creating_session(self):
        import random
        import json
        
        rnd= self.round_number
        import shared_out
        self.P1_descr = shared_out.description[2*(rnd-1)]
        self.P2_descr = shared_out.description[1+2*(rnd-1)]
        self.payoff1 = json.dumps(shared_out.payoffs1[rnd-1])
        self.payoff2 = json.dumps(shared_out.payoffs2[rnd-1])
        self.title_descr = shared_out.game_type[rnd-1]
        
        for g in self.get_groups():
            g.comp_colour = random.choice([True, False])
        
        
        
            
            
            
        
class Group(BaseGroup):
    comp_colour = models.BooleanField()
    def determine_payoffs(self):
        for p in self.get_players():
            p.set_payoffs()
class Player(BasePlayer):
    choice = models.BooleanField(choices=[[True, 'Red'], [False, 'Blue']], label='Please select your colour', widget=widgets.RadioSelectHorizontal)
    payoff_by_round = models.CurrencyField()
    def set_payoffs(self):
        import json
        
        if self.id_in_group == 1:
            P2_colour = self.group.get_player_by_id(2).choice
            payoffs = json.loads(self.subsession.payoff1)
            table = payoffs[self.group.comp_colour]
            col = table[P2_colour]
            self.payoff_by_round = col[self.choice]
        if self.id_in_group == 2:
            P1_colour = self.group.get_player_by_id(1).choice
            payoffs = json.loads(self.subsession.payoff2)
            table = payoffs[self.group.comp_colour]
            col = table[self.choice]
            self.payoff_by_round = col[P1_colour]