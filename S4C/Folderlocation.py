'''
Created on Mar 4, 2019

@author: I325952
'''
#!/usr/bin/python
import re
import zlib
import urllib.request
import urllib
import sys

Path = ' '.join(sys.argv[1:])

# Need to identify the path in execution engine where file upload will happen
#Path = "/Users\i325952\OneDrive - SAP SE\Desktop\Faktura - 90007854.pdf"

extracted = b''
temp = b''
n = 0
lists = list()
try:
    bytestream = open(Path, "rb").read()
except:
    print("FileNotFoundError: [Errno 2] No such file or directory, Please correct the path")
else:    
    compiled = re.compile(rb'.*?FlateDecode.*?stream(.*?)endstream', re.S)
    
    for s in compiled.findall(bytestream):
        s = s.strip(b'\r\n')
        try:
            parts = zlib.decompress(s)
            for sub in parts.split(b"ET"):
                if b"BT" in sub:
                    for div in sub.split(b")Tj"):
                        if b"(" in div:
                            lists.append(div[div.find(b"(")+1:])
                            if (b"Artifact" in div) and (b":" in div) :
                                temp = lists[n-1]
                                lists[n-1] = lists[n]
                                lists[n] = temp
                            n = n + 1
        except:
            pass
    for i in range(len(lists)):
        extracted = extracted + b' ' + lists[i]        
        
    try:
        extracted = (extracted.split(b"\x00")[0]).decode("utf-8")
        extracted = extracted.replace('\\374', 'ü')
        extracted = extracted.replace('\\241', '¡')
        extracted = extracted.replace('\\242', '¢')
        extracted = extracted.replace('\\243', '£')
        extracted = extracted.replace('\\244', '¤')
        extracted = extracted.replace('\\245', '¥')
        extracted = extracted.replace('\\246', '¦')
        extracted = extracted.replace('\\247', '§')
        extracted = extracted.replace('\\250', '¨')
        extracted = extracted.replace('\\251', '©')
        extracted = extracted.replace('\\252', 'ª')
        extracted = extracted.replace('\\253', '«')
        extracted = extracted.replace('\\254', '¬')
        extracted = extracted.replace('\\255', '­')
        extracted = extracted.replace('\\256', '®')
        extracted = extracted.replace('\\257', '¯')
        extracted = extracted.replace('\\260', '°')
        extracted = extracted.replace('\\261', '±')
        extracted = extracted.replace('\\262', '²')
        extracted = extracted.replace('\\263', '³')
        extracted = extracted.replace('\\264', '´')
        extracted = extracted.replace('\\265', 'µ')
        extracted = extracted.replace('\\266', '¶')
        extracted = extracted.replace('\\267', '·')
        extracted = extracted.replace('\\270', '¸')
        extracted = extracted.replace('\\271', '¹')
        extracted = extracted.replace('\\272', 'º')
        extracted = extracted.replace('\\273', '»')
        extracted = extracted.replace('\\274', '¼')
        extracted = extracted.replace('\\275', '½')
        extracted = extracted.replace('\\276', '¾')
        extracted = extracted.replace('\\277', '¿')
        extracted = extracted.replace('\\300', 'À')
        extracted = extracted.replace('\\301', 'Á')
        extracted = extracted.replace('\\302', 'Â')
        extracted = extracted.replace('\\303', 'Ã')
        extracted = extracted.replace('\\304', 'Ä')
        extracted = extracted.replace('\\305', 'Å')
        extracted = extracted.replace('\\306', 'Æ')
        extracted = extracted.replace('\\307', 'Ç')
        extracted = extracted.replace('\\310', 'È')
        extracted = extracted.replace('\\311', 'É')
        extracted = extracted.replace('\\312', 'Ê')
        extracted = extracted.replace('\\313', 'Ë')
        extracted = extracted.replace('\\314', 'Ì')
        extracted = extracted.replace('\\315', 'Í')
        extracted = extracted.replace('\\316', 'Î')
        extracted = extracted.replace('\\317', 'Ï')
        extracted = extracted.replace('\\320', 'Ð')
        extracted = extracted.replace('\\321', 'Ñ')
        extracted = extracted.replace('\\322', 'Ò')
        extracted = extracted.replace('\\323', 'Ó')
        extracted = extracted.replace('\\324', 'Ô')
        extracted = extracted.replace('\\325', 'Õ')
        extracted = extracted.replace('\\326', 'Ö')
        extracted = extracted.replace('\\327', '×')
        extracted = extracted.replace('\\330', 'Ø')
        extracted = extracted.replace('\\331', 'Ù')
        extracted = extracted.replace('\\332', 'Ú')
        extracted = extracted.replace('\\333', 'Û')
        extracted = extracted.replace('\\334', 'Ü')
        extracted = extracted.replace('\\335', 'Ý')
        extracted = extracted.replace('\\336', 'Þ')
        extracted = extracted.replace('\\337', 'ß')
        extracted = extracted.replace('\\340', 'à')
        extracted = extracted.replace('\\341', 'á')
        extracted = extracted.replace('\\342', 'â')
        extracted = extracted.replace('\\343', 'ã')
        extracted = extracted.replace('\\344', 'ä')
        extracted = extracted.replace('\\345', 'å')
        extracted = extracted.replace('\\346', 'æ')
        extracted = extracted.replace('\\347', 'ç')
        extracted = extracted.replace('\\350', 'è')
        extracted = extracted.replace('\\351', 'é')
        extracted = extracted.replace('\\352', 'ê')
        extracted = extracted.replace('\\353', 'ë')
        extracted = extracted.replace('\\354', 'ì')
        extracted = extracted.replace('\\355', 'í')
        extracted = extracted.replace('\\356', 'î')
        extracted = extracted.replace('\\357', 'ï')
        extracted = extracted.replace('\\360', 'ð')
        extracted = extracted.replace('\\361', 'ñ')
        extracted = extracted.replace('\\362', 'ò')
        extracted = extracted.replace('\\363', 'ó')
        extracted = extracted.replace('\\364', 'ô')
        extracted = extracted.replace('\\365', 'õ')
        extracted = extracted.replace('\\366', 'ö')
        extracted = extracted.replace('\\367', '÷')
        extracted = extracted.replace('\\370', 'ø')
        extracted = extracted.replace('\\371', 'ù')
        extracted = extracted.replace('\\372', 'ú')
        extracted = extracted.replace('\\373', 'û')
        extracted = extracted.replace('\\374', 'ü')
        extracted = extracted.replace('\\375', 'ý')
        extracted = extracted.replace('\\376', 'þ')
        extracted = extracted.replace('\\377', 'ÿ')
        if ("\\" in extracted):
            if ("\\\\" not in extracted):
                extracted = extracted.replace('\\', '')
        print(extracted)
    
    except:
        pass
