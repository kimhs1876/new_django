from titanic.models.dataset import Dataset
import pandas as pd


class Service(object):

    dataset = Dataset()

<<<<<<< HEAD
    def new_model(self, payload) -> object: #?
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname) #?

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) #?

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] #?

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis= 1 )
=======
    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
        this.test = this.test.drop([feature], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
<<<<<<< HEAD
        this.train['Embarked'] = this.train['Embarked'].map({'S':1,'C':2,'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S':1,'C':2,'Q':3})
=======
        this.train['Embarked'] =  this.train['Embarked'].map({'S':1,'C':2,'Q':3})
        this.test['Embarked'] =  this.test['Embarked'].map({'S':1,'C':2,'Q':3})
>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        return this

    @staticmethod
    def fare_band_fill_na(this) -> object:
        return this

    @staticmethod
<<<<<<< HEAD
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False) #?
=======
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
<<<<<<< HEAD
=======
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
<<<<<<< HEAD
    def gender_nominal(this) -> object:
=======
    def gender_norminal(this) -> object:
>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)
        this.train = combine[0]
        this.test = combine[1]
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        return this

    @staticmethod
    def create_k_fold(this) -> object:
        return
<<<<<<< HEAD
=======

>>>>>>> 4fc54fa54ad8a3abe242235691d868ffbd89423d
