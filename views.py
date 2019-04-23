from app import app
from user import user
from fileUp import fileUp
from city import city

app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(fileUp,url_prefix='/fileUp')
app.register_blueprint(city,url_prefix='/city')