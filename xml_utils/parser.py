from lxml import etree


# FALSE POSITIVE TEST: safe parser passed as variable — should NOT fire
# Our xml_external_entity rule now only fires on single-argument lxml calls
def safe_parse(source: str):
    parser = etree.XMLParser(resolve_entities=False)
    return etree.parse(source, parser)


# TRUE POSITIVE: no parser argument — uses lxml defaults
def unsafe_parse(source: str):
    return etree.parse(source)
