import web

urls = (
    '/(.*)', 'application.controllers.cook.Cooki'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()