from omegaconf import DictConfig
from omegaconf import OmegaConf


def my_app(cfg: DictConfig) -> None:
    """
    Testing omegaconf config
    :param cfg:
    :return:
    """
    print(OmegaConf.to_yaml(cfg))
    print(cfg)


if __name__ == "__main__":
    config = OmegaConf.load("config_example.yaml")
    my_app(config)