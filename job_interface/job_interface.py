from abc import ABC, abstractmethod


class JobInterface(ABC):
    @abstractmethod
    def execute(self):
        """Method that all jobs must implement"""
        pass

    @abstractmethod
    def get_status(self):
        """Return the status of the job"""
        pass

    @abstractmethod
    def update_status(self, new_status):
        """Update the status of the job"""
        pass
