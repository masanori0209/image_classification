import logging
import json
import os
import imghdr
import numpy as np
import requests
import tempfile
import uuid
from bottle import Bottle, route, request, HTTPResponse, debug

model = None
app = Bottle()
debug(True)

@app.route('/ai/v1', method=['POST'])
def image_classification():
    # 保存したモデルを読み込んで、予測する
    def ai_check(path):
        try:
            from keras import models, backend
            from keras.preprocessing.image import load_img, img_to_array
            from keras.applications.resnet50 import preprocess_input
            global model
            if model is None:
                #学習済みモデルの読込
                model = models.load_model('image_classification.h5')
            #画像の読込
            img_path = (path)
            img = img_to_array(load_img(img_path))
            img= np.expand_dims(img, axis=0)
            img= preprocess_input(img)
            pred = model.predict(img)
            #判別結果で最も高い数値を抜き出し
            score = np.max(pred)
            #表示
            print('name :', np.argmax(pred[0]))
            print('score:', score)
            return int(np.argmax(pred[0])), float(score)
        except:
            import traceback
            traceback.print_exc()
            raise
    try:
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
            return returnResponse(
                200,
                json.dumps({
                    "success": True,
                    "message": "success",
                    "estimated_data": {
                        "class": _class,
                        "confidence": confidence
                    }
                })
            )
        else:
            tempdir.cleanup()
            return returnResponse(
                200,
                json.dumps({
                    "success": False,
                    "message": "Error",
                    "estimated_data": {}
                })
            )
    except:
        import traceback
        traceback.print_exc()
        return returnResponse(
            400,
            json.dumps({
                "success": False,
                "message": "Error",
                "estimated_data": {}
            })
        )

def returnResponse(status, response):
    r = HTTPResponse(status=status, body=response)
    r.set_header("Content-Type", "application/json")
    return r