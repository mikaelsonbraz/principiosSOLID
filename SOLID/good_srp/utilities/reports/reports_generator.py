class ReportsGenerator:
    '''
    BAD OCP PRINCIPLE

    @classmethod
    def build(cls, type, repos):
        if str(type).upper.__eq__("HTML"):
            return HTMLGenerator.build(repos)
        elif str(type).upper.__eq__("MD") or str(type).upper.__eq__("MARKDOWN"):
            return MarkdownGenerator.build(repos)
    '''

    
    "GOOD OCP PRINCIPLE"

    @classmethod
    def build(cls, generator, repos):
        return generator.build(repos)