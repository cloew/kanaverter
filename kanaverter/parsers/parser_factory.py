from .grouped_parser import GroupedParser
from .parser_types import ParserTypes
from .readings_after_parser import ReadingsAfterParser

type_to_parser_class = {
    ParserTypes.group: GroupedParser,
    ParserTypes.readings_after: ReadingsAfterParser,
}

def build_parser_for_type(parser_type):
    """ Builds the corresponding Parser for the given type """
    return type_to_parser_class[parser_type]()
