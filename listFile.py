import json
import os

def getSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size

def pathTree(path):
    fp = None
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        #d['type'] = "directory"
        d['member'] = [pathTree(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        #d['type'] = "file"
        fp = open(path, 'rb')
        d['size'] = str(getSize(fp)) + ' bytes'
    return d

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps(pathTree('/mnt/demo'))
    }
