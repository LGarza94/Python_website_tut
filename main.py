from website import create_app

app = create_app()

if __name__ == '__main__': 
    app.run(debug=True) #debug = True, if any change occurs to code, will rerun the web-server