import os

import pandas as pd
pd.set_option('display.max_columns', None)
file_dir = "./dataset"  # file directory
all_csv_list = os.listdir(file_dir)  # get csv list
for single_csv in all_csv_list:
    single_data_frame = pd.read_csv(os.path.join(file_dir, single_csv))
    #     print(single_data_frame.info())
    if single_csv == all_csv_list[0]:
        all_data_frame = single_data_frame
    else:  # concatenate all csv to a single dataframe, ingore index
        all_data_frame = pd.concat([all_data_frame, single_data_frame], ignore_index=True)
data = all_data_frame
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
highlist=data.nlargest(3, 'Like')
print(highlist)
counter=data.value_counts('Uname')
print(counter.index[0], counter[0])
print(data.shape[0])
print(data['Uid'].unique().shape[0])
print(data.shape[0]/data['Uid'].unique().shape[0])
counter=data.value_counts('Content')
print(counter.index[0], counter[0])
