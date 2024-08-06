# TIA-manual

#### Explain:

###### Tia is a program developed by Ahmed Youssef that works to translate images and comics into Arabic. Its goal is to break the language barrier that hinders public life.

##### ![sorece program](https://github.com/ahmed4sy/Transimgs-sorece)

#### Config:

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
