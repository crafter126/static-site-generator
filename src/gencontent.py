import os
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(md: str) -> str:
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")


def generate_page(
    from_path: str, template_path: str, dest_path: str | Path, basepath: str
) -> None:
    print(f"* {from_path} {dest_path} -> {template_path}")

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="', f'href="{basepath}')
    template_content = template_content.replace('src="', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template_content)


def generate_pages_resursive(
    dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str
) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_resursive(from_path, template_path, dest_path, basepath)
