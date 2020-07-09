from omegaconf import DictConfig
from omegaconf import OmegaConf


def my_app(cfg: DictConfig) -> None:
    """
    Testing omegaconf config
    :param cfg:
    :return:
    """
    print(cfg.pretty())
    print(cfg)


if __name__ == "__main__":
    config = OmegaConf.load("config_example.yaml")
    my_app(config)