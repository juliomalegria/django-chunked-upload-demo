from django.urls import path
from demo.views import ChunkedUploadDemo, MyChunkedUploadView, MyChunkedUploadCompleteView

urlpatterns = [
    path('', ChunkedUploadDemo.as_view(), name='chunked_upload'),
    path('api/chunked_upload_complete/', MyChunkedUploadCompleteView.as_view(), name='api_chunked_upload_complete'),
    path('api/chunked_upload/', MyChunkedUploadView.as_view(), name='api_chunked_upload'),

]
