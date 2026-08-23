import very_smart_markdown_parser

# TODO: add argparse

hardware_pills = {
    "hackclub": "assets/HackClub.png",
    "ibom": "assets/iBom.png",
    "kicanvas": "assets/KiCanvas.png",
    "onshape": "assets/OnShape.png",
}

with open("README.md", "r") as f:
    readme_content = f.read()


parsed_title = very_smart_markdown_parser.get_title(readme_content)
name = input(f"Project name (current: {parsed_title}): ")
if name == "":
    name = parsed_title

parsed_description = very_smart_markdown_parser.get_description(readme_content)
description = input(f"Project description (current: {parsed_description}): ")
if description == "":
    description = parsed_description

readme_content = very_smart_markdown_parser.replace_title(readme_content, name)
readme_content = very_smart_markdown_parser.replace_description(
    readme_content, description
)

with open("README.md", "w") as f:
    f.write(readme_content)

print("Project name:", name)
