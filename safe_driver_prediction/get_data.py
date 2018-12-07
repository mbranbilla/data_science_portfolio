# For linux and MacOS
# Require kaggle Api: can be installed by 'pip install kaggle'
# https://www.kaggle.com/docs/api
# Data comes from
# https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/data

import os

sh_command = '''
    kaggle competitions download -c porto-seguro-safe-driver-prediction

    7za x sample_submission.7z
    7za x train.7z
    7za x test.7z

    if [ -d "data" ]; then
        rm data/*
    else
        mkdir data
    fi

    mv sample_submission.csv train.csv test.csv data/
    rm *.7z
'''

os.system(sh_command)
