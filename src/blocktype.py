import re
from enum import Enum



class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h1"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"




def markdown_to_blocks(markdown):
    if markdown is None: return []
    if len(markdown.strip()) == 0: return []

    blocks = []
    for txt in markdown.split("\n\n"):
        if len(txt.strip()) == 0: continue
        blocks.append(txt.strip())

    return blocks

# will use proper regex to extract the text from the markdown 
def get_block_text(block, block_type):
    match(block_type):
        case BlockType.CODE:
            return __get_code_text(block)
        case BlockType.HEADING:
            return __get_heading_text(block)
        case BlockType.QUOTE:
            return __get_quote_text(block)
        case BlockType.UNORDERED_LIST:
            return __get_unordered_text(block)
        case BlockType.ORDERED_LIST:
            return __get_ordered_text(block)
        case BlockType.PARAGRAPH:
            return [block.replace("\n", " ")]
        case _:
            raise Exception(f"Block type {block_type} is not supported")


def __build_extract(pattern):
    def extract(markdown):
        return re.findall(pattern, markdown)
    return extract

__get_quote_text = __build_extract(r"\>([\ \w]+)")
__get_heading_text = __build_extract(r"(#{1,6})([\ \w]+)")
__get_code_text = __build_extract(r"```\n([\W\w\n]+)```")
__get_unordered_text = __build_extract(r"\- ([\ \w]+)")
__get_ordered_text = __build_extract(r"\d+\. ([\ \w]+)")


def block_to_block_type(block):
    if block == None: raise ValueError("Argument cannot be NULL")
    if len(block.strip()) == 0: raise ValueError("Argument should not be blank")

    text = block.strip()
    if __is_match_heading(text): return BlockType.HEADING
    if __is_match_code(text): return BlockType.CODE
    if __is_quote_block(text): return BlockType.QUOTE
    if __is_unordered_list(text): return BlockType.UNORDERED_LIST
    if __is_ordered_list(text): return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def __build_regex(pattern):
    def is_match(test):
        result = re.search(pattern, test)
        if result == None: return False
        return len(result.string) > 0
    return is_match

__is_match_quote = __build_regex(r"\>[\ \w]+")
__is_match_heading = __build_regex(r"#{1,6}[\ \w]+")
__is_match_code = __build_regex(r"```[\W\w]+```")
__is_match_unordered = __build_regex(r"\- [\ \w]+")
__is_match_ordered = __build_regex(r"\d+\. [\ \w]+")

def __is_quote_block(text):
    if len(text) == 0: return False

    for line in text.split("\n"):
        if not __is_match_quote(line.strip()): return False

    return True

def __is_unordered_list(text):
    if len(text) == 0: return False

    # each line must start with hyphen and space
    for line in text.split("\n"):
        if not __is_match_unordered(line.strip()): return False

    return True

def __is_ordered_list(text):
    if len(text) == 0: return False

    # each line must start with number, period, and space
    for line in text.split("\n"):
        if not __is_match_ordered(line.strip()): return False
    
    return True
