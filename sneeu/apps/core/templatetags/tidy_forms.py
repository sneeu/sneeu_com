from django.template import Context, Library, Node, TemplateSyntaxError, \
    resolve_variable
from django.template.loader import get_template


register = Library()


class FieldNode(Node):
    def __init__(self, field):
        self.field = field

    def render(self, context):
        actual_field = resolve_variable(self.field, context)
        template = get_template('core/_field.html')
        context = Context({
            'field': actual_field,
            'field_type': type(actual_field.field.widget).__name__,
        })
        return template.render(context)


def do_field(parser, token):
    try:
        tag_name, field = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]

    return FieldNode(field)


register.tag('field', do_field)
