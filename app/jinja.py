from jinja2 import FileSystemLoader, Environment

loder = FileSystemLoader('templates')
env = Environment(loader=loder)
template = env.get_template('index.html')

file = open('output/index.html', 'w')

render = template.render(title="Floky Sys - Sistema de Monitoramento", name="Floky")
file.write(render)
file.close()