from lango.matcher import match_rules
from mycroft.skills.common_query_skill import CommonQuerySkill, CQSMatchLevel
from nlquery.nlquery import NLQueryEngine
from nlquery.utils import first

class WikidataSkill(CommonQuerySkill):
    def __init__(self):
        super().__init__()
        self.engine = NLQueryEngine('localhost', 9000)
        self.engine.logger = self.log

    def CQS_match_query_phrase(self, utt):
        sent = self.engine.preprocess(utt)
        tree = self.engine.parser.parse(sent)
        if len(tree) == 0:
            return
        ans = first([
            match_rules(tree, self.engine.find_entity_rules, self.engine.find_entity_query),
            match_rules(tree, self.engine.subject_prop_rules, self.engine.subject_query),
        ])
        if ans and ans.data:
            return (utt, CQSMatchLevel.GENERAL, ans.to_plain())

def create_skill():
    return WikidataSkill()

