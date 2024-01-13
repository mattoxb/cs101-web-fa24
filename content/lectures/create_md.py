import yaml

def create_markdown_files_from_yaml(yaml_file):
    # Read and parse the YAML file
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    weight = 1

    for key, value in data.items():
        title = value['title']
        slug = value['slug']
        date = value['date']

        # Create the Markdown file
        filename = f"{slug}.md"
        with open(filename, 'w') as md_file:
            md_content = (
                f"---\n"
                f"title: \"{title}\"\n"
                f"date: {date}T16:18:22-06:00\n"
                f"draft: false\n"
                f"weight: {weight}\n"
                f"---\n"
            )
            md_file.write(md_content)

        weight += 1

# Example usage
create_markdown_files_from_yaml('../../data/lectures.yml')
