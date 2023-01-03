from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)

#     from flaskblog import app, db
# >>> app.app_context().push()
# >>> db.create_all()