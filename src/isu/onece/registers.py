from .interfaces import IFlowDocument, IAccumulatorRegister
from zope.interface import implementer


class RegisterBase:
    pass


class AccumulatorRegisterBase(RegisterBase):
    pass


@implementer(IAccumulatorRegister)
class AccumulatorRegister(AccumulatorRegisterBase):
    """Accumulates amounts by means of
    accumulating document's data.
    """

    def __init__(self):
        super(AccumulatorRegister, self).__init__()
        self._documents = []
        self._balance = 0

    def add(self, doc):
        assert IFlowDocument.providedBy(
            doc), "argument must be IFLowDocument provider"
        self._documents.append(doc)
        # TODO: request all transactions
        self._balance += self._get_amount(doc)
        return doc

    def _get_amount(self, doc, asxes=None):
        db = doc.amount()
        if not doc.receipt:
            db = -db
        return db

    def remove(self, doc):
        assert IFlowDocument.providedBy(
            doc), "argument must be IFlowDocumentDocument provider"
        self._documents.remove(doc)
        self._balance -= self._get_amount(doc)  # TODO: request all
        return doc

    def documents(self, filter=None):
        return self._documents

    def balance(self, date=None, axes=None):
        # TODO: date and axes must be supplied explicitly.
        return self._balance
