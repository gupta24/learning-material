import os
import sys
import threading
import logging
import boto3
from pathlib import Path
from botocore.exceptions import ClientError




class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


class Operations:
    def __init__(self, bucket_name, key_path) -> None:
        self.s3 = boto3.client("s3", 
                aws_access_key_id="AKIATVK36G73ZO5G6GFO",
                aws_secret_access_key="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"
                )
        self.bucket = bucket_name 
        self.key = key_path

    


class CrudOperation(Operations):
    # make the crud operation on file and folder..

    def upload_file(self, file_name) -> bool:
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if self.key is None:
            self.key = os.path.basename(file_name)

        try:
            response = self.s3.upload_file(file_name, self.bucket, self.key,  Callback=ProgressPercentage(filename=file_name))
        except ClientError as e:
            logging.error(e)
            return False
        return True


    def upload_fileobj(self, file_name) -> bool:
        """Upload a file object to an S3 bucket

        :param file_name: File name to upload
        :return: True if file was uploaded, else False
        """

        try:
            with open(file_name, "rb") as f:
                response = self.s3.upload_fileobj(f, self.bucket, self.key)
        except Exception as e:
            logging.error(e)
            return False
        return True


    def upload_folder(self, folder_name) -> bool:
        """Upload a folder object to an S3 bucket

        :param folder_name: Folder name to upload
        :return: True if folder with subfolder and files was uploaded, else False
        """

        try:
            response = self.s3.put_object(Bucket=self.bucket, Key=(self.key+folder_name+'/'))
        except Exception as e:
            logging.error(e)
            return False
        return True

    
    def get_object(self, file_or_folder_name):
        """Get a file or folder object from an S3 bucket

        :param file_or_folder_name: File or Folder name to get
        :return: data object if file or folder name is available, else False
        """

        try:
            response = self.s3.get_object(Bucket=self.bucket, Prefix=self.key, Key=file_or_folder_name)
            data = response['Body'].read()
        except Exception as e:
            logging.error(e)
            return False
        return data


    def get_list_object(self, folder_name=None):
        """Get a list of file or folder object from an S3 bucket

        :param folder_name: Folder name to get list object
        :return: data object if file or folder name is available, else False
        """

        if folder_name:
            self.key = self.key+folder_name+"/"

        try:
            response = self.s3.list_objects(Bucket=self.bucket, Prefix=self.key)
        except ClientError as e:
            logging.error(e)
            return False

        data = response.get("Contents")
        for file in data:
            print(f"Key: {file['Key']}")
        return data



    def get_list_file_using_paginator(self, folder_name=None, max_items=None, page_size=None, starting_token=None):
        """Get a list of file or folder object using paginator from an S3 bucket

        :param folder_name: Folder name to get list object
        :return: data object if file or folder name is available, else False
        """

        if folder_name:
            self.key = self.key+folder_name+"/"

        try:    
            paginator = self.s3.get_paginator("list_objects")
            response = paginator.paginate(Bucket=self.bucket, Prefix=self.key, PaginationConfig={
                "MaxItems": max_items,
                "PageSize": page_size,
                "StartingToken": starting_token})
        except ClientError as e:
            logging.error(e)
            return False

        for page in response:
            files = page.get("Contents")
            for file in files:
                print(f"Key: {file['Key']}")
        return response

    

    def delete_object(self, object_name):
        """Delete a file or folder object from an S3 bucket

        :param object_name: Object name to get list object
        :return: data object if file or folder name is available, else False
        """

        try:
            resource = self.s3.delete_object(Bucket=self.bucket, Key=self.key+object_name+"/")
        except ClientError as e:
            logging.error(e)
            return False
        return True


    def delete_all_object(self, folder_name):
        """Delete a file or folder object from an S3 bucket

        :param folder_name: Folder name to get list object
        :return: True if file or folder name are deleted successfully, else False
        """

        try:
            response = self.s3.list_objects(Bucket=self.bucket, Prefix=self.key+folder_name+"/")
            files_in_folder = response["Contents"]
            files_to_delete = []
            # We will create Key array to pass to delete_objects function
            for f in files_in_folder:
                files_to_delete.append({"Key": f["Key"]})
            # This will delete all files in a folder
            response = self.s3.delete_objects(
                Bucket=self.bucket, Delete={"Objects": files_to_delete}
            )
        except ClientError as e:
            logging.error(e)
            return False
        return True


    
    def download_object_from_s3(self, s3path, localPath=None, overwrite_existing_file=True):
        """Download a file object from an S3 bucket

        :param file_name: File name to get list object
        :return: True if file or file name are download successfully, else False
        """

        if 's3://' not in s3path:
            print('Given path is not a valid s3 path.')
            raise Exception('Given path is not a valid s3 path.')

        s3_tokens = s3path.split('/')
        bucket_name = s3_tokens[2]
        object_path = ""
        filename = s3_tokens[-1]
        print('Filename: ' + filename)

        if len(s3_tokens) > 4:
            for tokn in range(3, len(s3_tokens) - 1):
                object_path += s3_tokens[tokn] + "/"
            object_path += filename
        else:
            object_path += filename
        print('object: ' + object_path)
        try:
            if not overwrite_existing_file and Path.is_file(filename):
                pass
            else:
                if localPath is None:
                    self.s3.download_file(bucket_name, object_path, filename)
                else:
                    self.s3.download_file(bucket_name, object_path, localPath + '/' + filename)
        except ClientError as e:
            logging.error(e)
            return False
        return True





if __name__ == "__main__":
    bucket_name = input("set the bucket name : ")
    key_name = input("set the key path name : ") #"name/ofyour/folders/"
    op_obj = CrudOperation(bucket_name=bucket_name, key_path=key_name)
    func = input("set the function name that you want to run : ")
    path_or_folder_name = input("give the path or s3 : ")
    res_data = op_obj.func(s3path=path_or_folder_name)
 
    if res_data:
        print("object operate successfully")
    else:
        print("object operate failed!")
    