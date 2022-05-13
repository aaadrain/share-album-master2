from flask import Flask
from api import bp
import os
static_path = (os.path.dirname(__file__),'static')
app = Flask(
    __name__,
    static_folder='static',
)
app.register_blueprint(bp, url_prefix='/')
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    # 生产状态可以把debug调成False
    app.run(host='192.168.0.103', port=8000, debug=True,ssl_context=('./server.crt','./server.key'))
