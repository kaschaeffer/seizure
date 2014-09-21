from boto.s3 import connection
import seizure.config

class KaggleToS3(Object):
    def __init__(self, 
                 aws_access_key, 
                 aws_secret_key, 
                 chunk_size=1024)
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.chunk_size     = chunk_size
        self.connection     = connection.S3Connection(aws_access_key, 
                                                      aws_secret_key)

    def transfer_from_urls(urls):
        for url in urls:
            transfer_from_url(url)

    def transfer_from_url(url):
        pass

    def upload_chunk(chunk, key):
        pass

    def download_chunk(url):
        # TODO
        return chunk


def main():
    pass

if __name__ == '__main__':
    main()
