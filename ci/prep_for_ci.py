import click
import yaml


@click.command()
@click.option("--config")
@click.option("--data")
def main(config: str, data: str):
    """Set the config to run for many epochs to test overfitting."""
    with open(config) as f:
        cfg = yaml.safe_load(f.read())

    cfg["wandb_project"] = "ci-llm-finetuning-overfit-sqlqa"
    cfg["seed"] = 117  # always set a seed

    num_epochs = 50
    val_set_size = 0.5

    cfg["val_set_size"] = val_set_size
    cfg["num_epochs"] = num_epochs
    cfg["eval_steps"] = num_epochs // 10
    cfg.pop("evals_per_epoch", None)  # incompatible with eval_steps
    cfg.pop("sample_packing", False)  # requires larger dataset

    with open(config, "w") as f:
        yaml.dump(cfg, f)


if __name__ == "__main__":
    main()
