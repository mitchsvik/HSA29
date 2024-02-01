"""Lambda function to handle S3 events"""
import io

from urllib import parse

import boto3
from PIL import Image


def convert_to_other_type(object_body: io.BytesIO, key: str, new_mime_type: str):
    """Converts an JPEG image to BMP/GIF/PNG format"""
    object_body.seek(0)

    image = Image.open(object_body, mode='r')
    if new_mime_type == 'image/bmp':
        image = image.convert('1')
    elif new_mime_type == 'image/gif':
        image = image.convert('P')
    elif new_mime_type == 'image/png':
        image = image.convert('RGBA')
    image.save('/tmp/temp_image', new_mime_type.split('/')[1])
    s3_client = boto3.client('s3')

    mime_ending = new_mime_type.split('/')[1]
    s3_client.upload_file(
        '/tmp/temp_image', 'hsa29-media-bucket', f'{mime_ending}/{key}.{mime_ending}' )
    return 0


def s3_media_handler(event, context):
    """Handles S3 events"""
    _ = event, context
    s3_client = boto3.client('s3')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        key = parse.unquote(key)

        # object_head = s3_client.head_object(Bucket=bucket, Key=key)
        # mime_type = object_head['ContentType']

        object_body = io.BytesIO(s3_client.get_object(Bucket=bucket, Key=key)['Body'].read())
        convert_to_other_type(object_body, key, 'image/bmp')
        convert_to_other_type(object_body, key, 'image/gif')
        convert_to_other_type(object_body, key, 'image/png')
    return 0
