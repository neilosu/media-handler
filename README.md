# media-handler

## Run
```
python chat_app/manage.py runserver
```

## API
### image upload
```
curl --location 'http://127.0.0.1:8000/media/upload/' --form 'image=@"/path/to/image_name.jpg"'
```
### Image retrieve
```
curl --location 'http://127.0.0.1:8000/media/image/test.png'
```
### Thumbnail image retrieve
```
curl --location 'http://127.0.0.1:8000/media/thumbnail/test.png'
```

## Notes
You can click on the thumbnail image after you upload the image to view the original image.
