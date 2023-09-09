import lib.log as log, lib.color as color, lib.config as conf


config = {
    "bot": {
        "version": "3.0",
        "status_type": "dnd",
        "status_playing": "Have fun :)!"
    },

    "paths": {
        "secrets_config": "config/secrets.yml",
        "logs_config": "config/log_config.yml",
    },

    "harassment": {
        "target_guild_id": 0,
        "target_user_id": 0,
        "event_timer": 30,
        "random_messages": True,

        "timeout_time_lower": 10,
        "timeout_time_upper": 20,

        "mute_time_lower": 10,
        "mute_time_upper": 15,

        "deafen_time_lower": 5,
        "deafen_time_upper": 10,

        "lockout_time_lower": 5,
        "lockout_time_upper": 15,
    }
}

secrets = {
    "token": "",
}

class Config:
    def __init__(self, config_yml: str) -> None:
        self.config_yml = config_yml
        conf.create_config(self.config_yml, config)
        self.config = conf.get_config(self.config_yml)

        self.secrets_yml = self.config["paths"]["secrets_config"]
        conf.create_config(self.secrets_yml, secrets)
        self.secrets = conf.get_config(self.secrets_yml)


        self.bot__version = self.config["bot"]["version"]
        self.bot__status_type = self.config["bot"]["status_type"].lower()
        self.bot__status_playing = self.config["bot"]["status_playing"]

        self.path__logs_config = self.config["paths"]["logs_config"]

        self.harassment__target_guild_id = self.config["harassment"]["target_guild_id"]
        self.harassment__target_user_id = self.config["harassment"]["target_user_id"]
        self.harassment__event_timer = self.config["harassment"]["event_timer"]
        self.harassment__random_messages = self.config["harassment"]["random_messages"]

        self.harassment__timeout_time_lower = self.config["harassment"]["timeout_time_lower"]
        self.harassment__timeout_time_upper = self.config["harassment"]["timeout_time_upper"]

        self.harassment__mute_time_lower = self.config["harassment"]["mute_time_lower"]
        self.harassment__mute_time_upper = self.config["harassment"]["mute_time_upper"]

        self.harassment__deafen_time_lower = self.config["harassment"]["deafen_time_lower"]
        self.harassment__deafen_time_upper = self.config["harassment"]["deafen_time_upper"]

        self.harassment__lockout_time_lower = self.config["harassment"]["lockout_time_lower"]
        self.harassment__lockout_time_upper = self.config["harassment"]["lockout_time_upper"]

        self.token = self.secrets["token"]

    def reload_config(self):
        self.config = conf.get_config(self.config_yml)

        self.secrets_yml = self.config["paths"]["secrets_config"]
        self.secrets = conf.get_config(self.secrets_yml)

        self.bot__version = self.config["bot"]["version"]
        self.bot__status_type = self.config["bot"]["status_type"].lower()
        self.bot__status_playing = self.config["bot"]["status_playing"]

        self.path__logs_config = self.config["paths"]["logs_config"]

        self.harassment__target_guild_id = self.config["harassment"]["target_guild_id"]
        self.harassment__target_user_id = self.config["harassment"]["target_user_id"]
        self.harassment__event_timer = self.config["harassment"]["event_timer"]
        self.harassment__random_messages = self.config["harassment"]["random_messages"]

        self.harassment__timeout_time_lower = self.config["harassment"]["timeout_time_lower"]
        self.harassment__timeout_time_upper = self.config["harassment"]["timeout_time_upper"]

        self.harassment__mute_time_lower = self.config["harassment"]["mute_time_lower"]
        self.harassment__mute_time_upper = self.config["harassment"]["mute_time_upper"]

        self.harassment__deafen_time_lower = self.config["harassment"]["deafen_time_lower"]
        self.harassment__deafen_time_upper = self.config["harassment"]["deafen_time_upper"]

        self.harassment__lockout_time_lower = self.config["harassment"]["lockout_time_lower"]
        self.harassment__lockout_time_upper = self.config["harassment"]["lockout_time_upper"]

        self.token = self.secrets["token"]