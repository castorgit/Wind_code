"""
.. module:: RandomForestDirRegressionArchitecture

RandomForestDirRegressionArchitecture
*************

:Description: RandomForestDirRegressionArchitecture

    

:Authors: HPAI-BSC
    

:Version: 

:Created on: 29/05/2019 12:21 

"""


from Wind.Architectures.SCKArchitecture import SCKArchitecture
from sklearn.ensemble import RandomForestRegressor

__author__ = 'HPAI-BSC'

class RandomForestDirRegressionArchitecture(SCKArchitecture):
    """Direct regression architecture based on random forest
    """
    data_mode = ('2D', '0D')  #
    modname = 'RFDIRREG'

    def generate_model(self):
        """
        Generates the model

        -------------
        json config:

        "arch": {
            "n_estimators" : number of trees
            "max_features": number of features to consider when looking for the best split
            "oob_score": whether to use out-of-bag samples to estimate the R^2 on unseen data
            "mode": "RF_dir_reg"

        }

        The rest of the parameters are the defaults of scikit-learn
        -------------

        :return:
        """
        self.model = RandomForestRegressor(n_estimators=self.config['arch']['n_estimators'],
                                         max_features=self.config['arch']['max_features'],
                                           oob_score=self.config['arch']['oob_score'],n_jobs=-1)
