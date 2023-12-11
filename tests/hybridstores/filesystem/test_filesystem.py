import unittest
from langchain.embeddings import FakeEmbeddings

from hybridagi import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        # Initialize a Redis client and the RedisGraphHybridStore
        self.redis_url = "redis://localhost:6379"
        self.index_name = "test"
        self.verbose = False
        self.embeddings = FakeEmbeddings(size=512)
        self.embeddings_dim = 512
        # Set up the RedisGraphHybridStore
        self.filesystem = FileSystem(
            redis_url = self.redis_url,
            index_name = self.index_name,
            embeddings = self.embeddings,
            embeddings_dim = self.embeddings_dim,
            verbose = self.verbose
        )
        self.filesystem.clear()
        self.filesystem.initialize()

    def test_add_document(self):
        self.filesystem.add_documents(
            ["/home/user/text.txt"],
            ["This is a document"],
            languages = ["plaintext"]
        )

