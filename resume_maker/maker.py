import yaml
import jinja2
import os


def get_resume_data(file_path):
    """
    Return a dictionary of yaml configurables.
    :param str file_path: path to yaml file
    :return: Dictionary of yaml configuration
    :rtype: dict
    """
    with open("config.yaml", "r") as f:
        return yaml.load(f.read())


def generate_output(data, template_path):
    """

    :param data:
    :param template_path:
    :return:
    """
    # Jinja2 identification strings conflict with LaTex
    # http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
    jina_env = jinja2.Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    template = jina_env.get_template(template_path)
    return template.render(**data)


def write_file(text, output_path):
    with open(output_path, "w") as f:
        f.write(text)


output = generate_output(get_resume_data("config.yaml"), "templates/dead_simple_cv.tex")
write_file(output, "output.tex")

