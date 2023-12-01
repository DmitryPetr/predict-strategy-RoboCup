import pandas as pd
import numpy as np

dfNUmber = ['472', '898', '1690']

lenResultDf = 3060
numPeople = 11
gridLen = 6
gridWidth = 4

#generalDf = pd.read_csv(f'./general_df_process_more_{lenResultDf}_withHead.csv', ',')
#generalDf = pd.read_csv(f'./general_df_process_more_{lenResultDf}_withHead_withHidden.csv', ',')
#generalDf = pd.read_csv(f'./dataGeneral/general_df_process_more_{lenResultDf}_withHead.csv', ',')
generalDf = pd.read_csv(f'./general_df_process_more_{lenResultDf}_withHead_withMerged.csv', ',')

print('Start df: ', len(generalDf))

#     if (stats[statistic] < 120):
#         print('drop stats: ', statistic, stats[statistic])
#        # print('drop stats test: ', resFlagsTeam[resFlagsTeam['strategyOpponent'] == statistic])
#         resFlagsTeam = resFlagsTeam.drop(resFlagsTeam[resFlagsTeam['strategyOpponent'] == statistic].index)

print('test check one: ', len(generalDf[np.isnan(generalDf['yBall']) | np.isnan(generalDf['xBall'])]))

generalDf = generalDf.drop(generalDf[np.isnan(generalDf['yBall']) | np.isnan(generalDf['xBall'])].index)
#generalDf = generalDf.drop(generalDf[(generalDf[np.isnan(generalDf['xBall'])])].index)

print('after drop nan ball coords: ', len(generalDf))

generalDf = generalDf.drop(
    generalDf[
        (generalDf.yBall > 32.0) |
        (generalDf.yBall < -32.0) |
        (generalDf.xBall > 54.0) |
        (generalDf.xBall < -54.0)
        ].index
)
#generalDf = generalDf.drop(generalDf[(generalDf[np.isnan(generalDf['xBall'])])].index)

print('after drop overflow ball coords: ', len(generalDf))


generalDf.to_csv(
    f'./general_df_process_more_{len(generalDf)}_withHead.csv',
    index=False
)

generalDf.to_csv(
    f'./general_df_process_more_{len(generalDf)}_withoutHead.csv',
    index=False, header=False
)

# generalDf.to_csv(
#     f'./general_df_process_more_{len(generalDf)}_withHead_withHidden.csv',
#     index=False
# )
#
# generalDf.to_csv(
#     f'./general_df_process_more_{len(generalDf)}_withoutHead_withHidden.csv',
#     index=False, header=False
# )
