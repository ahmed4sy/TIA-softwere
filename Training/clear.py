import os
print(
    os.popen("ls tesstrain/data/{}-ground-truth | grep eng_{}.lstmf".format("wild",4)).read().strip() == "eng_4.lstmf"
)