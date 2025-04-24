from kafka import KafkaProducer
import time
from tqdm import tqdm
import json

producer = KafkaProducer(bootstrap_servers='13.125.197.73:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for i in tqdm(range(10000)):
    msg = {"msg" : str(i)}
    producer.send('quickstart-seo', msg)
    # 100개마다 한 번씩 flush
    if (i + 1) % 100 == 0:
        producer.flush()
    # 0.01초 대기
    time.sleep(0.01)
    
producer.flush()
producer.close()
print('All messages sent and producer closed')

