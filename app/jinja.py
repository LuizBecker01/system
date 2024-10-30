from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader('templates')
env = Environment(loader=loader)
template = env.get_template('index.html')

file = open('output/index.html', 'w')

render = template.render(title="Floky Sys - Sistema de Monitoramento", name="Floky")
file.write(render)
file.close()