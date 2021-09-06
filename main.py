from pyzbar.pyzbar import decode, Decoded
from pyzbar.locations import Rect
from PIL import Image
import argparse

def get_coordinates(polygon_data: list) -> dict:
    """
    Gives the coordinates of the qr code as dict

    Args:
        polygon_data: list of points of the coordinates
    
    Returns: 
        dictionary of coordinates
    """
    coordinates = dict()
    for i,point in enumerate(polygon_data):
        coordinates.update({'x' + str(i): point.x})
        coordinates.update({'y' + str(i): point.y})
    return coordinates

def format_data(decoded_data: Decoded) -> dict:
    """
    Formats the decoded data and returns dictionary with encoded text and coordinates

    Args:
        decoded_data: data returned by pyzbar decoder
    
    Returns: 
        dictionary with formatted data
    """
    formatted_data = get_coordinates(decoded_data.polygon)
    text = decoded_data.data.decode('utf-8')
    formatted_data.update({'text': text})
    return formatted_data

def parse_qr(img_path: str) -> list:
    """
    Parse the qr codes

    Args:
        img_path: path of the image
    
    Returns: 
        list of decoded data
    """
    decoded_data_list = decode(Image.open(img_path))
    data = []
    for decoded_data in decoded_data_list:
        formatted_data = format_data(decoded_data)
        data.append(formatted_data)
    return data

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-I", "--image", required=True, help="Path of Image with QR Code")
    args = vars(ap.parse_args())
    img_path = args["image"]
    # parse the qr code
    data = parse_qr(img_path)
    print(data)
