import os
# allgt = open(f"Training/tesstrain/data/{file['name-type']}/all-gt","w")
# allstm = open(f"Training/tesstrain/data/{file['name-type']}/all-lstmf","w")
for num in range(1,29):
    os.system(
        f"tesseract Training/tesstrain/data/wild/eng_{num}.tif Training/tesstrain/data/wild-ground-truth/eng_{num} lstm.train"
    )

#     if (os.popen("ls Training/tesstrain/data/{}-ground-truth | grep eng_{}.lstmf".format(file['name-type'],num)).read().strip() == "eng_{}.lstmf".format(num)):
#             allgt.write(line)
#             allstm.write("Training/tesstrain/data/{}-ground-truth/eng_{}.lstmf \n".format(file['name-type'],num))
#     else:
#             os.remove("Training/tesstrain/data/{}-ground-truth/eng_{}.lstmf".format(file['name-type'],num))
# allgt.close()
# allstm.close()