import web
from datetime import datetime
from datetime import date




class Cooki:
    def GET(self, name):
      try:
        cooki = web.cookies()
        now = datetime.now()
        formato = now.strftime('Año: %Y, Mes: %h, Dia: %d, Hora: %H, Minutos: %M, Segundos: %S')

        if not name:
          name = 'Anonimo'
          web.setcookie("name",name)
        

        if cooki.get('visitas'):
          visitas = int(cooki.get('visitas'))
          visitas +=1
          web.setcookie('visitas', str(visitas))
         
        return "COOKIES: " + "    " + "Visitas: " + str(visitas) + ","+ " " + "Nombre: " + name +"," + " " + "Ultima visita: "+str(formato) + "."
        
      except Exception as e:
        return "Error" + str(e.args)


