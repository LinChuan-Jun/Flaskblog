from flaskblog import app
from flaskblog import db

with app.app_context():
    db.create_all()  # 在應用程式上下文內執行
    
if __name__ == '__main__':
    app.run(debug=True)