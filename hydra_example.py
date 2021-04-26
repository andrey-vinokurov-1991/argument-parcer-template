import hydra
from omegaconf import DictConfig
from omegaconf import OmegaConf


@hydra.main(config_name="config_example.yaml")
def my_app(cfg: DictConfig) -> None:
    """
    Testing hydra lib
    :param cfg:
    :return:
    """
    print(OmegaConf.to_yaml(cfg))
    print(cfg)


if __name__ == "__main__":
    my_app()
