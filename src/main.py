import util
import generate

util.copy_tree('static', 'public')
generate.generate_pages_recursive('content', 'template.html', 'public')