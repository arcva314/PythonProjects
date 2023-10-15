import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def match_predictor(match, model):
    team_info = list(match.items())
    team1data = team_info[0][1]
    team2data = team_info[1][1]
    predict_data = team1data + team2data
    prediction = model.predict([predict_data])
    if int(prediction) == 1:
        return team_info[0][0]
    else:
        return team_info[1][0]


nations_data = {'Belgium':[1,1,1], 'Portugal':[0.625,3,0.50208], 'Italy':[1,5,1], 'Austria':[0.6,18,0.62917],
                'France':[0.8,2,0.60417], 'Switzerland':[0.625,10,0.50208], 'Croatia':[0.625,13,0.50208],
                'Spain':[0.8,4,0.60417], 'Sweden':[0.6,11,0.62917], 'Ukraine':[0.75,14,0.575], 'England':[0.875,6,0.78958],
                'Germany':[0.875,9,0.647917], 'Netherlands':[0.75,8,0.85417], 'Czech Republic':[0.625,17,0.50208],
                'Wales':[0.5,12,0.42917], 'Denmark':[0.5,7,0.42917]}

R16_match_1 = {'Belgium':[1,1,1], 'Portugal':[0.625,3,0.50208]}
R16_match_2 = {'Italy':[1,5,1], 'Austria':[0.6,18,0.62917]}
R16_match_3 = {'France':[0.8,2,0.60417], 'Switzerland':[0.625,10,0.50208]}
R16_match_4 = {'Croatia':[0.625,13,0.50208], 'Spain':[0.8,4,0.60417]}
R16_match_5 = {'Sweden':[0.6,11,0.62917], 'Ukraine':[0.75,14,0.575]}
R16_match_6 = {'England':[0.875,6,0.78958], 'Germany':[0.875,9,0.647917]}
R16_match_7 = {'Netherlands':[0.75,8,0.85417], 'Czech Republic':[0.625,17,0.50208]}
R16_match_8 = {'Wales':[0.5,12,0.42917], 'Denmark':[0.5,7,0.42917]}

for i in range(1,11):
    #dictionaries to store matches
    QF_match_1 = {}
    QF_match_2 = {}
    QF_match_3 = {}
    QF_match_4 = {}
    SF_match_1 = {}
    SF_match_2 = {}
    Final = {}
    #create machine learning model
    f = open('prediction'+str(i), 'a')
    df = pd.read_excel('Euro 2021.xlsx', engine='openpyxl')
    df = df.drop(['Year', 'Team 1', 'Team 2', 'Team 1 GS Win Rate', 'Team 2 GS Win Rate'], 1)
    df.astype(float)
    X = np.array(df.drop(['Team 1 Win'], 1))
    y = np.array(df['Team 1 Win'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier(n_estimators=1000, max_depth=4)
    model.fit(X_train, y_train)

    #R16
    f.write('Round of 16 Matches\n\n')


    f.write('Match 1\n')
    f.write(str(list(R16_match_1.items())[0][0]) + ' vs. ' + str(list(R16_match_1.items())[1][0])+'\n')
    R16_match_1_winner = match_predictor(R16_match_1, model)
    f.write('Match 1 Winner: '+str(R16_match_1_winner)+'\n\n')

    f.write('Match 2\n')
    f.write(str(list(R16_match_2.items())[0][0]) + ' vs. ' + str(list(R16_match_2.items())[1][0]) + '\n')
    R16_match_2_winner = match_predictor(R16_match_2, model)
    f.write('Match 2 Winner: '+str(R16_match_2_winner)+'\n\n')

    QF_match_1.update({R16_match_1_winner:nations_data[R16_match_1_winner], R16_match_2_winner:nations_data[R16_match_2_winner]})

    f.write('Match 3\n')
    f.write(str(list(R16_match_3.items())[0][0]) + ' vs. ' + str(list(R16_match_3.items())[1][0]) + '\n')
    R16_match_3_winner = match_predictor(R16_match_3, model)
    f.write('Match 3 Winner: ' + str(R16_match_3_winner) + '\n\n')

    f.write('Match 4\n')
    f.write(str(list(R16_match_4.items())[0][0]) + ' vs. ' + str(list(R16_match_4.items())[1][0]) + '\n')
    R16_match_4_winner = match_predictor(R16_match_4, model)
    f.write('Match 4 Winner: ' + str(R16_match_4_winner) + '\n\n')

    QF_match_2.update({R16_match_3_winner:nations_data[R16_match_3_winner], R16_match_4_winner:nations_data[R16_match_4_winner]})

    f.write('Match 5\n')
    f.write(str(list(R16_match_5.items())[0][0]) + ' vs. ' + str(list(R16_match_5.items())[1][0]) + '\n')
    R16_match_5_winner = match_predictor(R16_match_5, model)
    f.write('Match 5 Winner: ' + str(R16_match_5_winner) + '\n\n')

    f.write('Match 6\n')
    f.write(str(list(R16_match_6.items())[0][0]) + ' vs. ' + str(list(R16_match_6.items())[1][0]) + '\n')
    R16_match_6_winner = match_predictor(R16_match_6, model)
    f.write('Match 6 Winner: ' + str(R16_match_6_winner) + '\n\n')

    QF_match_3.update({R16_match_5_winner:nations_data[R16_match_5_winner], R16_match_6_winner:nations_data[R16_match_6_winner]})

    f.write('Match 7\n')
    f.write(str(list(R16_match_7.items())[0][0]) + ' vs. ' + str(list(R16_match_7.items())[1][0]) + '\n')
    R16_match_7_winner = match_predictor(R16_match_7, model)
    f.write('Match 7 Winner: ' + str(R16_match_7_winner) + '\n\n')

    f.write('Match 8\n')
    f.write(str(list(R16_match_8.items())[0][0]) + ' vs. ' + str(list(R16_match_8.items())[1][0]) + '\n')
    R16_match_8_winner = match_predictor(R16_match_8, model)
    f.write('Match 8 Winner: ' + str(R16_match_8_winner) + '\n\n')

    QF_match_4.update({R16_match_7_winner:nations_data[R16_match_7_winner], R16_match_8_winner:nations_data[R16_match_8_winner]})

    #QF
    f.write('Quarter Finals\n\n')

    f.write('Match 1\n')
    f.write(str(list(QF_match_1.items())[0][0]) + ' vs. ' + str(list(QF_match_1.items())[1][0]) + '\n')
    QF_match_1_winner = match_predictor(QF_match_1, model)
    f.write('Match 1 Winner: '+ str(QF_match_1_winner) + '\n\n')

    f.write('Match 2\n')
    f.write(str(list(QF_match_2.items())[0][0]) + ' vs. ' + str(list(QF_match_2.items())[1][0]) + '\n')
    QF_match_2_winner = match_predictor(QF_match_2, model)
    f.write('Match 2 Winner: ' + str(QF_match_2_winner) + '\n\n')

    SF_match_1.update({QF_match_1_winner:nations_data[QF_match_1_winner], QF_match_2_winner:nations_data[QF_match_2_winner]})

    f.write('Match 3\n')
    f.write(str(list(QF_match_3.items())[0][0]) + ' vs. ' + str(list(QF_match_3.items())[1][0]) + '\n')
    QF_match_3_winner = match_predictor(QF_match_3, model)
    f.write('Match 3 Winner: ' + str(QF_match_3_winner) + '\n\n')

    f.write('Match 4\n')
    f.write(str(list(QF_match_4.items())[0][0]) + ' vs. ' + str(list(QF_match_4.items())[1][0]) + '\n')
    QF_match_4_winner = match_predictor(QF_match_4, model)
    f.write('Match 4 Winner: ' + str(QF_match_4_winner) + '\n\n')

    SF_match_2.update({QF_match_3_winner:nations_data[QF_match_3_winner], QF_match_4_winner:nations_data[QF_match_4_winner]})

    #SF
    f.write('Semi Finals\n\n')

    f.write('Match 1\n')
    f.write(str(list(SF_match_1.items())[0][0]) + ' vs. ' + str(list(SF_match_1.items())[1][0]) + '\n')
    SF_match_1_winner = match_predictor(SF_match_1, model)
    f.write('Match 1 Winner: '+ str(SF_match_1_winner) + '\n\n')

    f.write('Match 2\n')
    f.write(str(list(SF_match_2.items())[0][0]) + ' vs. ' + str(list(SF_match_2.items())[1][0]) + '\n')
    SF_match_2_winner = match_predictor(SF_match_2, model)
    f.write('Match 2 Winner: ' + str(SF_match_2_winner) + '\n\n')

    Final.update({SF_match_1_winner:nations_data[SF_match_1_winner], SF_match_2_winner:nations_data[SF_match_2_winner]})

    #Final
    f.write('Finals\n\n')
    f.write(str(list(Final.items())[0][0]) + ' vs. ' + str(list(Final.items())[1][0]) + '\n')
    Final_winner = match_predictor(Final, model)
    f.write('Final Winner: ' + str(Final_winner))
    f.close()
