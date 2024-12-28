import pytest
from abc import ABC, abstractmethod
from job_interface.job_interface import JobInterface


# Dummy implementation for testing
class DummyJob(JobInterface):
    def __init__(self):
        self.status = "pending"

    def execute(self):
        self.status = "completed"

    def get_status(self):
        return self.status

    def update_status(self, new_status):
        self.status = new_status


def test_job_interface_abstract_methods():
    # Assert that JobInterface cannot be instantiated directly
    with pytest.raises(TypeError):
        JobInterface()

    # Assert that a concrete class implementing JobInterface works
    job = DummyJob()
    assert job.get_status() == "pending"
    job.execute()
    assert job.get_status() == "completed"
    job.update_status("failed")
    assert job.get_status() == "failed"
