from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    sanitized_blocks = []
    for block in blocks:
        if block == "":
            continue
        sanitized_blocks.append(block.strip())
    return sanitized_blocks


def block_to_block_type(md: str) -> BlockType:
    lines = md.split("\n")

    if md.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0] == "```" and lines[-1] == "```":
        return BlockType.CODE
    if md.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if md.startswith("-"):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if md.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH
