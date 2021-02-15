from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1001321863
    OWNER_USERNAME = "atutal"
    API_KEY = "1525945197:AAH488rW5bSJSEAfEJtMdqM_OhRVq1vLH_Y"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/koindex_tlg_bot'
    MESSAGE_DUMP = '-1001338373390'
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1001321863]
    LOAD = []
    NO_LOAD = []
