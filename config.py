from pathlib import Path
class ProjectPaths:
    def __init__(self):
        self.root = Path(__file__).parent
        self.data = self.root / "assets"

        self.train_data = self.data / "sms_supervised_train.csv"
        self.unlabelled_data = self.data / "sms.unlabelled.csv"
        self.test_data = self.data / "sms_test.csv"
PATHS = ProjectPaths()