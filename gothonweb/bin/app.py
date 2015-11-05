import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.form()

    def POST(self):
        form = web.input(nome="Nessun nome", eta="Nessuna eta")
        nome = form.nome
        eta=form.eta
        if nome == "":
            nome = "Nessun nome."
        if eta == "":
            eta = "Nessuna eta."
        greeting = "%s %s" % (nome, eta)
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
