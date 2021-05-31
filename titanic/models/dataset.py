from dataclasses import dataclass


@dataclass
<<<<<<< HEAD
class Dataset(object):

=======
class Dataset(object): # practice more
>>>>>>> dcd8d7dd7232544c60e9c60c7813019f5622e2ea
    context: str
    fname: str
    train: str
    test: str
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @context.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @context.setter
    def label(self, label): self._label = label