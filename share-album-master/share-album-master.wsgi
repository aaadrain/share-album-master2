import sys

# app's path
# 就这个地方需要填自己项目对应的根目录
sys.path.insert(0, "E:\share-album-master\share-album-master")
from run import app

# Initialize WSGI app object
application = app
