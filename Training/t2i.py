import os
import json

# تحميل بيانات التدريب من ملف JSON
with open("trainig_data.json", "r") as js:
    file = json.loads(js.read())

# إنشاء المجلدات اللازمة
os.makedirs(f"Training/tesstrain/data/{file['name-type']}", exist_ok=True)
os.makedirs(f"Training/tesstrain/data/{file['name-type']}-ground-truth", exist_ok=True)

# فتح ملفات all-gt و all-lstmf للكتابة

    # قراءة ملف all-gt
with open("Training/all-gt", "r") as f:
    lines = f.readlines()
    num = 1
    for line in lines:
        # إنشاء ملف نصي مؤقت
        with open(f"{num}.txt", "w") as temp_file:
            temp_file.write(line)

        # إنشاء صورة من النص باستخدام text2image
        os.system(
            f"text2image --text={num}.txt --outputbase=Training/tesstrain/data/{file['name-type']}/eng_{num} --font={file['font-name']} --fonts_dir={file['font-path']}  --strip_unrenderable_words --max_pages=1 --leading=32 --xsize=3600 --ysize=480 --char_spacing=1.0 --exposure=0 --unicharset_file=Training/langdata/eng.unicharset"
        )

        # تشغيل tesseract لإنشاء ملف lstmf
        os.system(
            f"tesseract Training/tesstrain/data/{file['name-type']}/eng_{num}.tif Training/tesstrain/data/{file['name-type']}-ground-truth/eng_{num} lstm.train"
        )
        os.system(
            f"cp {num}.txt Training/tesstrain/data/{file['name-type']}-ground-truth/eng_{num}.gt.txt"
        )

        # التحقق مما إذا كان ملف lstmf تم إنشاؤه بشكل صحيح
        lstmf_path = f"Training/tesstrain/data/{file['name-type']}-ground-truth/eng_{num}.lstmf"
        if os.path.isfile(lstmf_path) == False:
            # حذف الملفات التالفة وتبعياتها
            os.remove(f"Training/tesstrain/data/{file['name-type']}/eng_{num}.tif")
            os.remove(f"Training/tesstrain/data/{file['name-type']}/eng_{num}.box")
            if os.path.isfile(lstmf_path):
                os.remove(lstmf_path)

        # حذف الملف النصي المؤقت
        os.remove(f"{num}.txt")

        num += 1

#os.system("cp Training/all-gt Training/tesstrain/data/{}/".format(file['name-type']))
