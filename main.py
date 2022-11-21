
from flask import Flask , request 
import json
from flask_restful import Api, Resource
import pandas as pd
import plotly.express as px
import plotly.io as pio
from functions import *

app = Flask(__name__)
api = Api(app)


api.add_resource(All_rows, '/<string:table_name>/')
api.add_resource(Row, '/<string:table_name>/<int:id>')
api.add_resource(Sort, '/<string:table_name>/sort/<string:field>')
api.add_resource(Search, '/<string:table_name>/search/<string:field>=<string:value>')
api.add_resource(Analysis, '/<string:table_name>/analysis/<string:field>')
if __name__ == '__main__':
    app.run(debug=True)