from grammar import Grammar
from ricky import snorkel_rules, snorkel_ops

class SemanticParser():
    def __init__(self):
        self.grammar = Grammar(rules=snorkel_rules, ops=snorkel_ops)

    def parse(self, explanations, user_lists={}, verbose=False, return_parses=False):
        """
        Accepts natural language explanations and returns parses
        """
        LFs = []
        parses = []
        for i, exp in enumerate(explanations):
            exp_parses = self.grammar.parse_input(exp, user_lists)
            for j, parse in enumerate(exp_parses):
                lf = self.grammar.evaluate(parse)
                if return_parses:
                    parse.function = lf
                    parses.append(parse)
                lf.__name__ = "exp%d_parse%d" % (i, j)
                LFs.append(lf)
        if return_parses:
            if verbose:
                print("{} parses created from {} explanations".format(len(LFs), len(explanations)))
            return parses
        else:
            if verbose:
                print("{} LFs created from {} explanations".format(len(LFs), len(explanations)))
            return LFs