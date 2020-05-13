from flask import request, jsonify, Blueprint, abort
from source import app
from source.firewalls import layer1, layer2, layer3, layer4
from source.views.dish import I_output_dish


@app.route('/dish', methods=['GET'])
@layer1.init_logging_system
# @layer2.permission_validation_system | No permission
@layer3.input_validation_system(interface={})
@layer4.output_validation_system(interface=I_output_dish)
def index(log_record_obj, validated_param):
    return {
        'code': 1000,
        'message': [
            {
                'dishId': 1,
                'brandName': 'Cuisine',
                'dishName': 'Bánh mì',
                'metricUnit': 'Cái',
                'dishPrice': 29000,
                'isOnDiscount': False,
                'discountDescription': '',
                'discountType': '',
                'discountAmount': 0,
                'recipeId': 1,
                'dishDescription': 'Fuck',
                'dishPopularity': 2,
                'dishScore': 4.6,
                'createDate': 1,
                'createById': 1,
                'gallery': ['https://hihi.com']
            }
        ]
    }
