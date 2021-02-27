from app import app
import flask_excel as excel

if __name__ == "__main__":
  excel.init_excel(app)
  app.run(host='127.0.0.1', port=5000)

