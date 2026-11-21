import logger

# inherit from this class to make special transferable data!
class data():
    def __init__(self):
        pass
    
    def log_data_driven(self):
        logger.log("This data has no value.")