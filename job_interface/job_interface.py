from abc import ABC, abstractmethod


class JobInterface(ABC):
    """Abstract base class for all jobs."""

    @abstractmethod
    def execute(self):
        """Execute the job."""
        pass

    @abstractmethod
    def get_status(self):
        """Return the status of the job."""
        pass

    @abstractmethod
    def update_status(self, new_status: str):
        """Update the status of the job."""
        pass

    def get_id(self):
        """Return the job ID."""
        pass
