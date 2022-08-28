from abc import ABC, abstractmethod


class Interface(ABC):
    """Interfaces of Interface, Concrete & Proxy should
    be the same, because the client should be able to use
    Concrete or Proxy without any change in their internals.
    """

    @abstractmethod
    def job_a(self, user: str) -> None:
        pass

    @abstractmethod
    def job_b(self, user: str) -> None:
        pass


class Concrete(Interface):
    """This is the main job doer. External services like
    payment gateways can be a good example.
    """

    def job_a(self, user: str) -> None:
        print(f"I am doing the job_a for {user}")

    def job_b(self, user: str) -> None:
        print(f"I am doing the job_b for {user}")


class Proxy(Interface):
    def __init__(self) -> None:
        self._concrete = Concrete()

    def job_a(self, user: str) -> None:
        print(f"I'm extending job_a for user {user}")

    def job_b(self, user: str) -> None:
        print(f"I'm extending job_b for user {user}")


class Gate:
    def __init__(self, sLock, sStatus) -> None:
        self._klass = Gate(self, sStatus)
        self.lock = sLock
        self.status = sStatus

    def open_method(self) -> None:
        pass

    def update_status(self, newStatus) -> String:
        self._klass.status = newStatus


class SecuredGate:
    def __init__(self) -> None:
        self._klass = Gate('Secured', null)
        self.key = sKey
        pass

    def open_method(self) -> None:
        print(f"Adding security measure to the method of {self._klass}")


if __name__ == "__main__":
    klass = Proxy()
    print(klass.job_a("red"))
    print(klass.job_b("nafi"))

gate = Gate('General', 'unLocked')
secured_gate = SecuredGate()
secured_gate.updateStatus('Locked')
secured_gate.open_method()
