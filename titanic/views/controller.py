from titanic.models.dataset import Dataset
from titanic.models.service import Service


class Controller(object):

    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_lable(this)
        this.train = service.create_train(this)
        return this # 데이터 프레임 !! 매우중요 !! 차트로 그리기 위해서 데이터프레임이여야 한다.

<<<<<<< HEAD
    def preprocess(self, train, test):
=======
    def preprocess(self, train) -> object: # Practice more
>>>>>>> dcd8d7dd7232544c60e9c60c7813019f5622e2ea
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train 의 type 은 {type(this.train)} 이다.')
        print(f'Train 의 column 은 {this.test.columns} 이다.')
        print(f'Test 의 type 은 {type(this.train)} 이다.')
        print(f'Test 의 column 은 {this.test.columns} 이다.')
        return this