from jinja2 import FileSystemLoader, Environment

loder = FileSystemLoader("templates")
env = Environment(loader=loder)
template = env.get_template("index.html")

file = open('output/index.html', 'w')

render = template.render(titule="Floky Sys - Sistema de Monitoramento", background_color="purple", text_color="white", nome="Floky")
file.write(render)
file.close()