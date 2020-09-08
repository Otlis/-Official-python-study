import time

from kafka import KafkaProducer


def main():
    ##生产模块
    producer = KafkaProducer(bootstrap_servers=['hadoop101:9092'])
    with open('D:\peoject\python\Official-python-study\mypyspark\my-from-kafka\mya.txt', 'r') as f:
        for line in f.readlines():
            time.sleep(1)
            producer.send("txt", line)
            print
            line
            # producer.flush()


if __name__ == '__main__':
    main()
