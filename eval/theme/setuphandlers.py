from collective.grok import gs
from eval.theme import MessageFactory as _

@gs.importstep(
    name=u'eval.theme', 
    title=_('eval.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eval.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
