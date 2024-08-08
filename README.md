# Translate Images All
![img](https://github.com/user-attachments/assets/9de328d4-ed2b-4b31-a18f-d32e49c7388e)
## Application:

TIA is a program developed by Ahmed Yousif that works to translate images and comics into Arabic. Its goal is to break the language barrier that hinders public life. ![sorece program](https://github.com/ahmed4sy/Transimgs-sorece)

Options:

```
  "init": It is a folder that contains two folders (inp: to insert images, out: to extract images after the program process is complete)
  "model": The type of engine that will take the texts from the image, and there are three so far.
  "key-api-OCR": Ocr.space private api key.
  "training-type": It is the name of the training file tesseract. ( auto:eng )
  "correct-text": Correcting words that come from ocr.
  "translate": The translation engine that will be used to translate the extracted texts is only two.
  "key-api-translate": huggingface.co private api key.
```
Config:

```json
{
  "init": "[ Folder images :: Take:str = [PATH] ]",
  "model": "[ model OCR :: Take:str = (tess-ocr,api-ocr,NLP) ]",
  "key-api-OCR": "[ API KEY OCR.space :: Take:str = [KEY] ]",
  "training-type": "[ name Train OCR :: Take:str = [NAME] ]",
  "correct-text": "[ correct text image :: Take:bool = (true,false) ]",
  "translate": "[ model Translate :: Take:str = (auto,NLP) ]",
  "key-api-translate": "[ API KEY Translate :: Take:str = [KEY] ]"
}
```

## Training:

## ICR:
## Build:

#### Install:
1. Java jre 17
2. python `3.10` & `pip install easyocr`
