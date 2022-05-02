from dynaconf import FlaskDynaconf


def config(app):
  FlaskDynaconf(app)
  return app
