from flask import Flask, render_template
from controllers.animales_controller import animales_bp

app=Flask(__name__,template_folder='views')

app.register_blueprint(animales_bp)



if __name__ == "__main__":
    app.run(debug=True)
