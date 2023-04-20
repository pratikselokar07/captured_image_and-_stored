import base64
from django.http import HttpResponse
from django.shortcuts import render
import base64
# Create your views here.
import cv2
import os
from django.conf import settings
import uuid
from datetime import datetime
from django.shortcuts import render


# import cv2
# import os

# def capture_image(request):
#     # Open the default camera
#     cap = cv2.VideoCapture(0)

#     # Read the image from the camera
#     ret, frame = cap.read()

#     # Release the camera
#     cap.release()

#     # Save the image to a folder
#     image_name = 'captured_image.jpg'
#     image_path = os.path.join(settings.MEDIA_ROOT, image_name)
#     cv2.imwrite(image_path, frame)

#     return HttpResponse('Image captured and saved successfully!')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
import base64
import os
import uuid
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def camera(request):
    if request.method == 'POST':
        img_data = request.POST.get('imgBase64')
        if img_data:
            img_data = img_data.replace('data:image/png;base64,', '')
            img_data = img_data.replace(' ', '+')
            img = base64.b64decode(img_data)
            img_name = str(uuid.uuid4()) + '.png'
            img_path = os.path.join('media', img_name)
            with open(img_path, 'wb') as f:
                f.write(img)
            photo = Photo(image=img_name)
            photo.save()
            return HttpResponse('Image saved successfully!')
    return render(request, 'camera.html')


