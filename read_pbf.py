import Ct_pb2
import sys

def read_pbf_file(file_path):
    with open(file_path, 'rb') as pbf_file:
        # Parse the PBF file using the generated protobuf module
        ct_root_message = Ct_pb2.CtRoot()
        ct_root_message.ParseFromString(pbf_file.read())

        # Access the data in the message
        for person in ct_root_message.ctRoot:
            #print(person)
            print(f"Person ID: {person._id}")
            print(f"Name: {person.name}")
            # Add more fields as needed

if __name__ == "__main__":
    # Provide the path to your PBF file
    pbf_file_path = 'sample.pbf'

    try:
        read_pbf_file(pbf_file_path)
    except Exception as e:
        print(f"Error reading the PBF file: {e}")
        sys.exit(1)