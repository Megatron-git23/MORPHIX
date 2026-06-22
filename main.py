import backend
import os

a = input("Enter file name to convert: ")

if not os.path.exists(a):
    print("File not found!")
    exit()

b = input("Convert to (pdf/json/csv/png/jpg): ").lower()

if b == "pdf":
    backend.convertToPdf(a, b)

elif b == "json":
    print("Only csv to json conversion possible ")
    backend.convertTojson(a, b)

elif b == "csv":
    print("Only json to csv conversion possible")
    backend.convertTocsv(a, b)

elif b in ["png", "jpg", "jpeg"]:
    backend.convertToPNG(a, b)

else:
    print("Unsupported format!")