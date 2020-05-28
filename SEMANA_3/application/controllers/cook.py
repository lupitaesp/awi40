import web
from datetime import datetime
from datetime import date




class Cooki:
    def GET(self, name):
      try:
        cookie = web.cookies()
        now = datetime.now()
        vista = 0
        formato = now.strftime('Año: %Y, Mes: %h, Dia: %d, Hora: %H, Minutos: %M, Segundos: %S')

        if not name:
          name = 'Anonimo'
          web.setcookie("name",name)
        

        if cookie.get('visitas'):
          visitas = int(cookie.get('visitas'))
          visitas +=1
          web.setcookie("visitas", str(visitas))
         
        return "COOKIES: " + "        " + "Visitas: " + str(visitas) + " " + "Nombre " + name + "Ultima entrada: "+str(formato)
        
      except Exception as e:
        return "Error" + str(e.args)


