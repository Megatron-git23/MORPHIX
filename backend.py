from docx2pdf import convert
from PIL import Image
import os
import pandas as pd


def convertToPdf(filename,suggest):
    filen=os.path.splitext(filename)[0] + ".pdf"
    convert(filename,filen)
    print("convertion finished")

def convertTojson(filename,suggest):
    df =pd.read_csv(filename)
    filen=os.path.splitext(filename)[0] + ".json"
    df.to_json(filen,orient="records")
    print("convertion completed")

def convertTocsv(filename,suggest):
    df = pd.read_json(filename)
    filen=os.path.splitext(filename)[0]+".csv"
    df.to_csv(filen,index=False)
    print("conversion completed")

def convertToPNG(filename,suggest):
    img=Image.open(filename)
    filen=os.path.splitext(filename)[0] + "." + suggest.lower()

    if(suggest.upper()=="JPG"):
       img=img.convert("RGB")

    img.save(filen,suggest.upper())
    print("conversion completed")
    

    
