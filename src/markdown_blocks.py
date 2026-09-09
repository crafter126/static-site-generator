def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    sanitized_blocks = []
    for block in blocks:
        if block == "":
            continue
        sanitized_blocks.append(block.strip())
    return sanitized_blocks
