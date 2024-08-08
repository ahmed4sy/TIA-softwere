# Translate Images All
![img](https://github.com/user-attachments/assets/9de328d4-ed2b-4b31-a18f-d32e49c7388e)
## Application:

> TIA is a program developed by ``Ahmed Yousif`` that works to translate images and comics into Arabic. Its goal is to break the language barrier that hinders public life. ![sorece program](https://github.com/ahmed4sy/Transimgs-sorece)

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
Each image you have processed has a folder with the same name in the `Extracting` folder that contains all the extracted data. There is an `ICR.txt` file with it. Correct the words in it using the `imgs` folder.<br />
After correcting all the letters, write this on the command line:
```shell
./ICR.sh [name-image]
```
The output will be the percentage between the OCR and the correct one, like:
```
ICR: 75%
```
> Note: If there is a distorted image that you do not want to include in the calculation, you must write a space like this `“  “`
## Build:
1. install Java `jre-17`.
2. install python `3.10` & `pip install easyocr`.
3. Make sure the command is present: `python3.10` and that it has this  `torch2.2.0+cpu` & `easyocr1.6.2` installed.
4. Fill in the `config.json` file correctly.
5. Run program `./App.sh` in Linux.
