import web

urls = (
    '/(.*)', 'application.controllers.cook.'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()