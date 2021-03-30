from src.client.app import create_app
from src.client.config import config

flask_app = create_app(config=config['development'])

if __name__ == '__main__':
    flask_app.run(debug=True)