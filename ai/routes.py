import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import json
import imghdr
import numpy as np
import requests
import tempfile
import uuid
from bottle import Bottle, route, request, HTTPResponse

app = Bottle()
# 仕様通りにレスポンス返すモックAPI
@app.route('/ai/v1', method=['POST'])
def image_classification():
    path = request.forms.get('path')
    response = requests.get('http://back:8000/image/' + path)
    tempdir = tempfile.TemporaryDirectory()
    tempfilepath = os.path.join(tempdir.name, str(uuid.uuid4()))
    image_type = None
    with open(tempfilepath, 'wb') as f:
        f.write(response.content)
    image_type = imghdr.what(tempfilepath)
    tempdir.cleanup()
    if image_type is not None:
        r = HTTPResponse(status=200, body={
            'success': True,
            'message': 'success',
            'estimated_data': {
                'class': 3,
                'confidence': 0.8683
            }
        })
        r.set_header("Content-Type", "application/json")
        return r
    else:
        r = HTTPResponse(status=200, body={
            'success': False,
            'message': 'Error:E50012',
            'estimated_data': {}
        })
        r.set_header("Content-Type", "application/json")
        return r

# キャッチアップ用に作成
# （途中）
@app.route('/ai/v2', method=['POST'])
def image_classification():
    # 保存したモデルを読み込んで、予測する
    def ai_check(path):
        from tensorflow.keras.preprocessing.image import img_to_array, load_img
        from tensorflow.keras.models import load_model
        #学習済みモデルの読込
        model = load_model('image_classification.h5')
        #画像の読込
        img_path = (path)
        img = img_to_array(load_img(img_path, target_size=(224,224)))
        #0-1に変換
        img_nad = img_to_array(img)/255
        #4次元配列に
        img_nad = img_nad[None, ...]
        #判別
        pred = model.predict(img_nad, batch_size=1, verbose=0)
        #判別結果で最も高い数値を抜き出し
        score = np.max(pred)
        #表示
        print('name :', np.argmax(pred[0]))
        print('score:', score)
        return np.argmax(pred[0]), score

    path = 'http://back:8000/image/{0}'.format(
        request.forms.get('path')
    )
    response = requests.get(path)
    tempdir = tempfile.TemporaryDirectory()
    tempfilepath = os.path.join(tempdir.name, str(uuid.uuid4()))
    image_type = None
    with open(tempfilepath, 'wb') as f:
        f.write(response.content)
    image_type = imghdr.what(tempfilepath)
    if image_type is not None:
        _class, confidence = ai_check(tempfilepath)
        tempdir.cleanup()
        return {
            'success': True,
            'message': 'success',
            'estimated_data': {
                'class': _class,
                'confidence': confidence
            }
        }
    else:
        tempdir.cleanup()
        return {
            'success': False,
            'message': 'Error:E50012',
            'estimated_data': {}
        }
    
