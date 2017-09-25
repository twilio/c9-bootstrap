from flask import Flask

app = Flask('bootcamp-app')


app.run(debug=True, host='0.0.0.0', port=8080)
