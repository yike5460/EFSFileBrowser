import json
import random
import string

def lambda_handler(event, context):
    for i in range(50):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(6, 12)))
        fp = None
        try:
            fp = open("/mnt/demo/" + ran_str + ".txt", 'w+')
            fp.write(''.join(random.sample(string.ascii_letters + string.digits, random.randint(24, 48))))
            fp.close()
        finally:
            if fp:
                fp.close()
    return {
        'statusCode': 200,
        'body': json.dumps("Successful writing random files:")
    }
